import { useNavigate } from "react-router-dom";

export function Landing() {
  const navigate = useNavigate(); 

  return (
    <>
      <div className="bg-background-secondary text-center h-screen min-h-96">
        {/* Landing header */}
        <div className=" absolute top-0 flex w-full h-16 text-t-secondary items-center justify-end px-6">
          <button 
            onClick={(e) => {navigate("/auth")}}
            className="font-akshar transition-colors text-2xl hover:text-t-primary hover:underline"
          >
            LOGIN
          </button>
        </div>
        
        {/* Landing body */}
        <div className="flex flex-col justify-center items-center w-fit h-full mx-auto">
          <b className="text-t-primary text-7xl mb-2">Spotify Vault</b>
          <h2 className="text-t-secondary text-3xl mb-9">
            personalized Spotify stat tracker
          </h2>
          <button 
            onClick={(e) => {navigate("/auth")}}
            className="font-akshar font-medium px-16 py-4 bg-bt-primary transition-colors hover:bg-bt-secondary hover:text-t-primary rounded-md text-xl text-t-tertiary"
          >LOG IN TO SPOTIFY
          </button>
        </div>
      </div>
    </>
  );
}
