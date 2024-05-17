import { redirectToAuthCodeFlow } from "../auth";

import icon from "../assets/icon.svg";

export function Landing() {
  return (
    <>
      <div className="bg-background-secondary text-center h-screen">
        <div className="absolute table w-full h-14 text-t-secondary text-center">
          <div className="table-cell align-middle text-left p-3 pl-7">
            <img src={icon} width="48" height="48"/>
          </div>
          <div className="table-cell align-middle text-right pr-7">
            <h1 className="font-['Akshar'] text-2xl">LOGIN/USER</h1>
          </div>
        </div>
        <div className="flex flex-col justify-center items-center w-fit h-full mx-auto">
          <b className="text-t-primary text-7xl mb-2">Spotify Vault</b>
          <h2 className="text-t-secondary text-3xl mb-9">
            personalized Spotify stat tracker
          </h2>
          <button 
            onClick={redirectToAuthCodeFlow}
            className="font-['Akshar'] font-medium px-16 py-4 bg-bt-primary transition-colors hover:bg-bt-secondary hover:text-t-primary rounded-md text-xl text-t-tertiary"
          >LOG IN TO SPOTIFY
          </button>
        </div>
      </div>
    </>
  );
}
