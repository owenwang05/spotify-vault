import { UserHeader } from "./Header";
import { useNavigate } from "react-router-dom";

export function NoAuth() {
  const navigate = useNavigate();

  return (
    <>
      <UserHeader/>
      <div className="flex flex-col min-h-96 h-screen bg-background-secondary">
        <b className="text-center mt-32 text-5xl w-full text-t-primary mb-3">Invalid Login</b>
        <button 
          onClick={() => {
            navigate("/");
          }}
          className="font-['Akshar'] font-medium px-16 py-4 mx-auto bg-bt-primary transition-colors hover:bg-bt-secondary hover:text-t-primary rounded-md text-xl text-t-tertiary"
          >RETURN HOME
        </button>
      </div>
    </>
  );
}