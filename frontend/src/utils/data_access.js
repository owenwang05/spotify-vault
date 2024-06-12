import { clearData, checkAPICode } from "./auth";
import Cookies from 'js-cookie'

const clientID = "84909814ef1c44faad1299269068aa6e";
const apiURL = "http://localhost:8000/api"

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

export async function getRecent(setData) {
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  console.log(Cookies.get('csrftoken'));

  const result = await fetch(`${apiURL}/recent/${accessToken}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': Cookies.get('csrftoken') 
    }
  });

  const response = await result.json(); 
  const data = JSON.stringify(response);
  localStorage.setItem('data', data);
  setData(response);
}

export async function getSnapshots(setSnapshots) {
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  const result = await fetch(`${apiURL}/snapshots/${accessToken}/`, {
    method: "GET",
  });

  const response = await result.json(); 
  const data = JSON.stringify(response);
  localStorage.setItem('snapshots', data);
  setSnapshots(response);
}

export function getSnapshot(index, setData) {

}

export function snapshotList(index, setSnapshots) {

}