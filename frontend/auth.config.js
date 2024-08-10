/* optionally create your own spotify app and change clientID to your own app's id
   The app's permission scope requires:
    user-read-private 
    user-read-email 
    user-top-read
    user-read-recently-played

  NOTE: if you look in package.json, npm run dev defaults to port 5173. This is 
  because the redirect uri configured in my Spotify Web API app is set to
  http://localhost:5173/, so that's the only uri that can work for auth.

  If you for some reason want to change the port or use a different host, create
  your own Spotify Web API app and configure package.json and this file yourself.
*/
export const clientID = "84909814ef1c44faad1299269068aa6e";

// set this to your backend api's url
export const apiURL = "http://localhost:8000/api"