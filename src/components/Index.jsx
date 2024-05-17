import { redirectToAuthCodeFlow } from "../auth";

export function Index() {
  return (
    <div className="bg-background-primary">
      <div className="flex flex-col justify-center items-center w-fit h-screen mx-auto">
        <h1 className="text-t-primary text-8xl mb-5">
          Spotify Vault
        </h1>
        <h2 className="text-t-secondary text-4xl mb-14">
          Personalized stat tracker for Spotify
        </h2>
        <button 
          onClick={redirectToAuthCodeFlow}
          className="px-16 py-4 bg-bt-primary transition-colors hover:bg-bt-secondary hover:text-t-primary rounded-md text-xl text-t-tertiary"
        >
          <b>Login to Spotify</b>
        </button>
      </div>
    </div>
  );
}