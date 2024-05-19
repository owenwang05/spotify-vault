import { clearData, checkAPICode } from "./auth";

function checkValidSession() {
  const expire = localStorage.getItem("expire");
  const accessToken = localStorage.getItem("access_token");
  const profile = localStorage.getItem("profile");

  if(profile && expire && accessToken && Date.now() < expire) {
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

export async function getTopSongs(setSongsLoaded){
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
  localStorage.setItem("top_songs", data);

  if(setSongsLoaded) setSongsLoaded(true);

  return response;
}

export async function getTopArtists(setArtistsLoaded){
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
  localStorage.setItem("top_artists", data);

  if(setArtistsLoaded) setArtistsLoaded(true);

  return response;
}