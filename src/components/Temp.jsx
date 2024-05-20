import { UserHeader } from "./Header";
import { useNavigate } from "react-router-dom";
import { clearData } from "../auth";

export function Temp() {
  const navigate = useNavigate();

  return (
    <>
      <UserHeader/>
      <div className="flex flex-col min-h-96 h-screen bg-background-secondary">
        <b className="text-center mt-32 text-5xl w-full text-t-primary mb-3">it works!!</b>
        <button 
          onClick={() => {
            navigate("/");
          }}
          className="font-['Akshar'] font-medium px-16 py-4 mx-auto bg-bt-primary transition-colors hover:bg-bt-secondary hover:text-t-primary rounded-md text-xl text-t-tertiary"
        >
            RETURN HOME
        </button>
        <button 
          onClick={clearData}
          className="mt-5 font-['Akshar'] font-medium px-16 py-4 mx-auto bg-bt-primary transition-colors hover:bg-bt-secondary hover:text-t-primary rounded-md text-xl text-t-tertiary"
        >
          CLEAR DATA
        </button>
        <button 
          onClick={() => {
            navigate("/user")
          }}
          className="mt-5 font-['Akshar'] font-medium px-16 py-4 mx-auto bg-bt-primary transition-colors hover:bg-bt-secondary hover:text-t-primary rounded-md text-xl text-t-tertiary"
        >
          GO TO USER PAGE
        </button>
        <button 
          onClick={() => {
            localStorage.setItem("expire", "1");
          }}
          className="mt-5 font-['Akshar'] font-medium px-16 py-4 mx-auto bg-bt-primary transition-colors hover:bg-bt-secondary hover:text-t-primary rounded-md text-xl text-t-tertiary"
        >
          SET EXPIRE
        </button>
      </div>
    </>
  );
}