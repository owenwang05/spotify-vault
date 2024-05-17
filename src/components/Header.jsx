import { Link } from "react-router-dom"

import icon from "../assets/icon.svg";

export function UserHeader() {
  return (
    <header className="bg-background-secondary pb-1 pl-auto pr-auto">
      <div className="table w-full h-10 bg-background-primary text-t-secondary text-center py-2">
        <div className="table-cell align-middle text-left">
          <div className="table-cell align-middle pl-4 pr-3">
            <Link to="/"><img src={icon} width="32" height="32"/></Link>
          </div>
          <div className="table-cell align-middle">
            <Link to="/"><h1 className="font-['Akshar'] text-1xl">SPOTIFY VAULT</h1></Link>
          </div>
        </div>

        <div className="table-cell align-middle text-right pr-4">
          <h1 className="font-['Akshar'] text-1xl">LOGIN/USER</h1>
        </div>
      </div>
    </header>
  );
}