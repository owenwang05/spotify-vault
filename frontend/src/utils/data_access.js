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

export async function createProfile(setData) {
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  await fetch(`${apiURL}/create/${accessToken}/`, {
    method: 'POST',
  });
}

export async function getRecent(setData) {
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  const result = await fetch(`${apiURL}/recent/${accessToken}/`, {
    method: 'POST',
  });

  const response = await result.json(); 
  const data = JSON.stringify(response);
  localStorage.setItem('data', data);
  setData(response);
}

export async function listSnapshots(setSnapshotList) {
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  const result = await fetch(`${apiURL}/snapshots/${accessToken}/`, {
    method: "GET",
  });

  const response = await result.json(); 
  const data = JSON.stringify(response);
  localStorage.setItem('snapshot_list', data);
  let array_conversion = []
  for(let i = 0; i < response.length; i++) {
    array_conversion.push(response[i]);
  }
  setSnapshotList(array_conversion);
}

export async function getSnapshot(index, setSnapshot) {
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  const result = await fetch(`${apiURL}/snapshots/${accessToken}/${index}`, {
    method: "GET",
  });

  const response = await result.json(); 
  const data = JSON.stringify(response);
  localStorage.setItem('snapshot', data);
  setSnapshot(response);
}

export async function saveSnapshot() {
  const accessToken = JSON.parse(localStorage.getItem("access_token")).access_token;
  try {
    await fetch(`${apiURL}/save/${accessToken}/`, {
      method: 'POST',
    });
  } catch(e) {
    console.error(e);
    return false;
  }

  return true;
}