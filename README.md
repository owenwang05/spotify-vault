# Spotify Vault 
A personalized daily Spotify stats tracker with the ability to save 24 hour profile snapshots of top genres, top songs, top artists, and listening time.

## Features 
**Authentication and Session Tracking:** Interfaces with the Spotify Web API's OAuth2.0 authorization flow so you can log in directly through Spotify. Keeps track of your session so you only need to log in once within an extended time period.

![2024-08-1001-50-33-CUT-ezgif-com-video-to-gif-converter.gif](https://i.postimg.cc/VN8CVZrk/2024-08-1001-50-33-CUT-ezgif-com-video-to-gif-converter.gif)

**View User Data:** See your profile's approximate listening data and top genres in the last 24 hours, as well as your top 5 songs and top 5 artists in the last 4 weeks.

![image.png](https://i.postimg.cc/1RJLYdtR/image.png)

**Save User Data:** Save the profile statistics you're currently viewing for later. You can save a profile snapshot once every 24 hours.

**Utilize the Backend API Seperately:** You can create your own front-end to interface with user snapshots and profile saving as they're implemented through a backend RESTful API.

<u>API Calls</u>:
- **/api/create/**
  - method: POST
  - headers:
    - Authorization: _\<Spotify Web API access token\>_
  - Creates a profile in the database for access to statistics and snapshot saving.
- **/api/recent/**
  - method: GET
  - headers:
    - Authorization: _\<Spotify Web API access token\>_
  - Returns JSON of a user's most recent data
- **/api/save/**
  - method: POST
  - headers:
    - Authorization: _\<Spotify Web API access token\>_
  - Saves a user's most recently viewed data
- **/api/delete/**
  - method: DELETE
  - headers:
    - Authorization: _\<Spotify Web API access token\>_
  - Deletes a user's profile
- **/api/snapshots/**
  - method: GET
  - headers:
    - Authorization: _\<Spotify Web API access token\>_
  - Returns a JSON list of all a user's snapshots and their date saved.
- **/api/snapshots/_\<snapshot index\>_/**
  - method: GET
  - headers:
    - Authorization: _\<Spotify Web API access token\>_
  - Returns JSON of the user's saved data.

## Tech Stack 
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=Django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black)
![React.js](https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black)

## Run Locally 
Clone the project

```bash
  git clone https://github.com/owen-wang-student/spotify-vault.git
```

### Back End API

cd into the backend directory
```bash
  cd backend
```

Start a virtual environment and install dependencies

```bash
  pip install -r requirements.txt
```

Create a postgres database

```SQL 
  psql
  CREATE DATABASE database_name;
```

Create a **.env** file in the backend directory
```bash
  └─backend
    ├─spotifyvault
    │  └─...
    ├─.env
    └─...
```

Define database information, a secret key, and domains allowed to make calls to the backend api in .env
```Dotenv
  # .env
  # postgres db host and port can be found with '\conninfo' in psql.
  DB_NAME = ...
  DB_USER = ...
  DB_PASSWORD = ...
  HOST = ...
  PORT = ...

  SECRET_KEY = your secret key
  ALLOWED_ORIGINS = ['domain1', 'domain2', ...]
```
Start the server

```bash
  python manage.py runserver
```

### Front End Website

cd into the frontend directory

```bash
  cd frontend
```

Install dependencies

```bash
  npm install
```

Set your backend API url and optionally set your own spotify app id in **auth.config.js**

``` bash
  └─frontend
    ├─src
    │  └─...
    ├─auth.config.js
    └─...
```
```js
  // auth.config.js
  export const clientID = ...
  export const apiURL = backend api url
```

Start the server

```bash
  npm run dev
```

## Authors

- Brandon Xu ([@bxrr](https://www.github.com/bxrr))
- Owen Wang ([@owen-wang-student](https://github.com/owen-wang-student))
