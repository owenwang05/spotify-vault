import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import { checkAPICode, clearData } from '../auth';

export function Auth() {
  const navigate = useNavigate();
  const params = new URLSearchParams(window.location.search);
  const error = params.get("error");

  useEffect(() => {(async () => {
    const status = error ? 0 : await checkAPICode();
    if(status) navigate("/user");
    else navigate("/");
  })()}, []);

  return (
    <>
      <div className='flex flex-col justify-center bg-background-secondary h-screen min-h-96 w-screen'>
        <h2 className='mx-auto text-t-secondary text-3xl'>redirecting...</h2>
      </div>
    </>
  )
}