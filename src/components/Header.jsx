import { Link, useNavigate } from "react-router-dom"
import { checkAPICode } from "../auth";

import icon from "../assets/icon.svg";

export function UserHeader() {
  const navigate = useNavigate();

  return (
    <header className="bg-background-secondary pb-1 pl-auto pr-auto">
      <div className="table w-full h-10 bg-background-primary text-t-secondary text-center py-2">
        <div className="table-cell align-middle text-left">
          <div className="table-cell align-middle pl-4 pr-3">
            <Link to="/">
              <img src={icon} width="32" height="32"/>
            </Link>
          </div>
          <div className="table-cell align-middle">
            <Link to="/" >
              <h1 
                className="font-['Akshar'] text-1xl transition-colors text-1xl hover:text-t-primary hover:underline"
                >SPOTIFY VAULT
              </h1>
            </Link>
          </div>
        </div>

        <div className="table-cell align-middle text-right pr-4">
        <button 
            onClick={(e) => {navigate("/auth")}}
            className="font-['Akshar'] transition-colors text-1xl hover:text-t-primary hover:underline"
          > LOGIN
        </button>
        </div>
      </div>
    </header>
  );
}