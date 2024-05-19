import { useState } from "react";
import { Link, useNavigate } from "react-router-dom"
import { clearData } from "../auth";

import icon from "../assets/icon.svg";

export function UserHeader() {
  const navigate = useNavigate();
  const profile = localStorage.getItem("profile");

  const [showPopup, setShowPopup] = useState(false);

  return (
    <header className="bg-background-secondary pb-1 pl-auto pr-auto">
      <div className="table w-full h-16 bg-background-primary text-t-secondary text-center ">
        <div className="table-cell align-middle text-left">
          <div className="table-cell align-middle pl-4 pr-3">
            <Link to="/">
              <img src={icon} width="48"/>
            </Link>
          </div>
          <div className="table-cell align-middle">
            <Link to="/" >
              <h1 
                className="font-['Akshar'] text-2xl transition-colors text-1xl hover:text-t-primary hover:underline"
                >SPOTIFY VAULT
              </h1>
            </Link>
          </div>
        </div>

        <div className="table-cell align-middle text-right pr-4">
          <button className="table-cell align-middle font-['Akshar'] transition-colors text-xl hover:text-t-primary hover:underline"
              onClick={(e) => {
                if(profile) {
                  setShowPopup((curState) => (!curState));
                } else {
                  navigate("/auth");
                }
              }}
            >{profile 
              ? <><img className="transition-border ease-in-out hover:border-3 border-white hover:duration-75 duration-50"
                  width="48"
                  src={JSON.parse(profile).images[0].url}
                  />
                </>
              : <>LOGIN</>}
          </button>
          {showPopup ? 
            <div className="flex flex-col absolute bg-background-primary right-4 border-3">
              <button className="w-full px-2 py-1"
                onClick={() => {
                  navigate("/temp")
                }}
              >Profile</button>
              <button className="w-full px-2 py-1"
                onClick={() => {
                  clearData();
                  navigate("/")
                }}
              >Log Out</button>
            </div>
            : <></>}
        </div>
      </div>
    </header>
  );
}