import { clearData, checkAPICode } from "./auth";

// this code is disgustingly bad

const clientID = "84909814ef1c44faad1299269068aa6e";

export async function checkValidSession() {
  const expire = localStorage.getItem("expire");
  const accessToken = localStorage.getItem("access_token");
  const profile = localStorage.getItem("profile");

  if(profile && expire && accessToken && Date.now() < expire) {
    return true;
  }
  await checkAPICode();
  return false;
}

export function getProfile(setProfile){  
  const profile = localStorage.getItem("profile");
  if(profile) {
    const response = JSON.parse(profile);
    setProfile(response);
    return response;
  }
  return {};
}

export async function getTopSongs(setSongs){
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  const result = await fetch("https://api.spotify.com/v1/me/top/tracks?offset=0&limit=5&time_range=short_term", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`
    },
  });
  
  const response = await result.json();
  const data = JSON.stringify(response);
  localStorage.setItem("top_songs", data);

  setSongs(response);

  return response;
}

export async function getTopArtists(setArtists){
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  const result = await fetch("https://api.spotify.com/v1/me/top/artists?offset=0&limit=5&time_range=short_term", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  
  const response = await result.json();
  const data = JSON.stringify(response);
  localStorage.setItem("top_artists", data);

  setArtists(response);

  return response;
}

export async function getListenTime(setListenTime){
  const startTime = Date.now() - 86400000; // set start time to one day before 
  const curTime = Date.now();  
  let totalTime = 0; 

  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token; // get access token 
  const result = await fetch(`https://api.spotify.com/v1/me/player/recently-played?limit=50&after=${startTime}`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`,
    }
  })

  const response = await result.json();
  const data = JSON.stringify(response);
  localStorage.setItem("recently_played", data);

  response.items.map((element) => {
    totalTime += element.track.duration_ms;
  })

  setListenTime(totalTime);
}

export async function getTopGenres() {
  
}