import { useState } from "react";
import { Link, useNavigate } from "react-router-dom"
import { clearData } from "../auth";

import icon from "../assets/icon.svg";

export function UserHeader() {
  const navigate = useNavigate();
  const profile = localStorage.getItem("profile");

  const [showPopup, setShowPopup] = useState(false);

  return (
    <header className="bg-background-secondary pl-auto pr-auto">
      <div className="flex w-full h-16 bg-background-secondary text-t-secondary items-center justify-between px-6">
        <div className="flex flex-row items-center gap-2">
          <Link to="/">
            <img src={icon} width="48"/>
          </Link>
          <Link to="/" >
            <h1 
              className="font-akshar text-2xl transition-colors text-1xl hover:text-t-primary hover:underline"
              >SPOTIFY VAULT
            </h1>
          </Link>
        </div>

        <div>
          <button className="table-cell align-middle font-akshar transition-colors text-xl hover:text-t-primary hover:underline"
              onClick={(e) => {
                if(profile) {
                  setShowPopup((curState) => (!curState));
                } else {
                  navigate("/auth");
                }
              }}
          >
            {profile ? 
                <div className="rounded-full overflow-hidden">
                  <img 
                    className={`transition-border object-contain rounded-full hover:duration-75 duration-50
                    ${showPopup 
                      ? 'border-t-primary border-4' 
                      : 'hover:border-4 border-t-secondary'}`
                    }
                    width="48"
                    src={JSON.parse(profile).images[0].url}
                  />
                </div>
              : 
                <div>
                  LOGIN
                </div>
            }
          </button>
          
          {showPopup ? 
            <div className="block w-36 absolute right-7 top-16 bg-background-primary p-4 rounded-md">
              <button 
                className="transition-all font-akshar text-right w-full px-2 py-1 hover:bg-background-tertiary border-l-0 border-background-primary hover:border-l-6 hover:border-bt-primary text-xl"
                onClick={() => {
                  setShowPopup(false);
                  navigate("/user")
                }}
              >
                Profile
              </button>
              <button 
                className="transition-all font-akshar text-right w-full px-2 py-1 hover:bg-background-tertiary border-l-0 hover:border-l-6 border-background-primary hover:border-bt-primary text-xl"
                onClick={() => {
                  setShowPopup(false);
                  clearData();
                  navigate("/")
                }}
              >
                Log Out
              </button>
              <button 
                className="transition-all font-akshar text-right w-full px-2 py-1 hover:bg-background-tertiary border-l-0 hover:border-l-6 border-background-primary hover:border-bt-primary text-xl"
                onClick={() => {
                  setShowPopup(false);
                  navigate("/temp")
                }}
              >
                Dev
              </button>
            </div>
            : null
          }
          
        </div>
      </div>
    </header>
  );
}