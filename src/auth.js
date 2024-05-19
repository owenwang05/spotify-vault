const clientID = "84909814ef1c44faad1299269068aa6e";
const redirectURI = "http://localhost:5173/auth";

// prevent user from being stuck in an authentication loop 
export function clearData()
{
  localStorage.setItem("verifier", "");
  localStorage.setItem("access_token", "");
  localStorage.setItem("expire", "");
  localStorage.setItem("profile", "");
  localStorage.setItem("top_songs", "");
  localStorage.setItem("top_artists", "");
}

export async function checkAPICode() {
  // if access token hasn't been set yet, then run code to retrieve data
  if(!localStorage.getItem("verifier")) {
    redirectToAuthCodeFlow();
    return 0;
  } else if(!localStorage.getItem("access_token")) {
    const params = new URLSearchParams(window.location.search);
    const code = params.get("code");
    if(!code) {
      redirectToAuthCodeFlow();
    }
    const token = await getAccessToken(code);
    const profile = await fetchProfile(token);
    return profile ? 1 : 0;
  } else {
    return 1;
  }
}

function generateCodeVerifier(length) {
  const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  const values = crypto.getRandomValues(new Uint8Array(length));
  return values.reduce((acc, x) => acc + possible[x % possible.length], "");
}

async function generateCodeChallenge(codeVerifier) {
  const data = new TextEncoder().encode(codeVerifier);
  const digest = await window.crypto.subtle.digest('SHA-256', data);
  return btoa(String.fromCharCode.apply(null, [...new Uint8Array(digest)]))
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=+$/, '');
}

// redirects user to spotify authenication page and returns to provided callback url
async function redirectToAuthCodeFlow() {
  clearData();
  const verifier = generateCodeVerifier(128);
  const challenge = await generateCodeChallenge(verifier);

  localStorage.setItem("verifier", verifier);

  const params = new URLSearchParams();
  params.append("client_id", clientID);
  params.append("response_type", "code");
  params.append("redirect_uri", redirectURI);
  params.append("scope", `
    user-read-private 
    user-read-email 
    user-top-read
    user-read-recently-played
    `);
  params.append("code_challenge_method", "S256");
  params.append("code_challenge", challenge);

  document.location = `https://accounts.spotify.com/authorize?${params.toString()}`;
}

// using authorization code fetch the spotify token api 
async function getAccessToken(code) {
  const verifier = localStorage.getItem("verifier");
  
  const params = new URLSearchParams();
  params.append("client_id", clientID);
  params.append("grant_type", "authorization_code");
  params.append("code", code);
  params.append("redirect_uri", redirectURI);
  params.append("code_verifier", verifier);

  const result = await fetch("https://accounts.spotify.com/api/token", {
    method: "POST",
    headers: { 
      "Content-Type": "application/x-www-form-urlencoded" 
    },
    body: params,
  });

  const response = await result.json();
  if(!response.access_token) return "";
  else {
    const data = JSON.stringify(response);
    localStorage.setItem("access_token", data);
    localStorage.setItem("expire", Date.now() + (response.expires_in-1) * 1000);

    return response.access_token;
  }
}

// fetch profile given 
async function fetchProfile(accessToken) {
  if (!accessToken) {
    console.error("No access token.");
    return null;
  }

  const result = await fetch("https://api.spotify.com/v1/me", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`
    },
  });
  const response = await result.json();
  const data = JSON.stringify(response);
  localStorage.setItem("profile", data);
  console.log(data);

  return response;
}