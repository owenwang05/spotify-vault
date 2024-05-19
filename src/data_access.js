import { clearData, checkAPICode } from "./auth";

function checkValidSession() {
  const expire = localStorage.getItem("expire");
  const accessToken = localStorage.getItem("access_token");

  if(accessToken && Date.now() < expire) {
    return true;
  }

  clearData();
  checkAPICode();
  return false;
}

function revalidateSession(){

}

async function getListenTime(){

}

export async function getTopSongs(){
  checkValidSession();

  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  const result = await fetch("https://api.spotify.com/v1/me/top/tracks", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`
    },
    params: {
      limit: 5,
      time_range: 'short_term',
    },
  });
  
  const response = await result.json();
  const data = JSON.stringify(response);
  localStorage.setItem("topSongs", data);

  return response;
}

export async function getTopArtists(){
  checkValidSession();

  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  const result = await fetch("https://api.spotify.com/v1/me/top/artists", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`
    },
    params: {
      limit: 5,
      time_range: 'short_term',
    },
  });
  
  const response = await result.json();
  const data = JSON.stringify(response);
  localStorage.setItem("topArtists", data);

  return response;
}