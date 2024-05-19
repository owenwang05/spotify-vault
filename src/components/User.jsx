import { useState, useEffect } from 'react';

import { UserHeader } from './Header'
import { getTopArtists, getTopSongs } from '../data_access'
import { clearData, checkAPICode } from '../auth';

export function User(){
  const [artistsLoaded, setArtistsLoaded] = useState(false);
  const [songsLoaded, setSongsLoaded] = useState(false);

  useEffect(() => {
    getTopArtists(setArtistsLoaded);
    getTopSongs(setSongsLoaded); 
  }, []);

  let topArtists = "";
  let topSongs = "";
  let profile = "";

  try {
    profile = JSON.parse(localStorage.getItem("profile"));
    if(!profile) throw new Error("Invalid profile");

    useEffect(() => {
      if(topArtists) topArtists = JSON.parse(localStorage.getItem("top_artists"));
    }, [artistsLoaded]);
    
    useEffect(() => {
      if(songsLoaded) topSongs = JSON.parse(localStorage.getItem("top_songs"));
    }, [songsLoaded]);
    } catch(e) {
      clearData();
      checkAPICode();
  }  

  return (
    <>
      <UserHeader />
      <section className="w-full h-full min-h-screen px-6 bg-background-secondary">
        <div className='flex flex-col gap-8 justify-center items-center max-w-6xl mx-auto'>
          <div className="flex flex-row items-center justify-start gap-12 w-full">
            <img 
              alt="profile picture"
              src={profile.images[1].url}
              className='w-75 rounded-full'
            />
            <h1 className="text-t-primary text-7xl font-medium font-akshar">
              {profile.display_name}
            </h1>
          </div>
          {artistsLoaded && songsLoaded
          ?<><div className="grid grid-cols-3 gap-8 w-full">
              <div className="h-96 bg-background-primary text-t-primary rounded-lg">
                <div className='p-6'>
                  <h1 className='text-3xl font-semibold'>Listening Time</h1>
                  <h1 className='text-3xl font-semibold'>Top Genres</h1>
                </div>
              </div>
              <div className="h-96 bg-background-primary text-t-primary rounded-lg">
                <div className='p-6'>
                  <h1 className='text-3xl font-semibold'>Top Songs</h1>
                  {}
                </div>
              </div>
              <div className="h-96 bg-background-primary text-t-primary rounded-lg">
                <div className='p-6'>
                  <h1 className='text-3xl font-semibold'>Top Artists</h1>
                </div>
              </div>
            </div>
    
            <div className='h-96 w-full bg-background-primary'>
              
            </div>
    
            <div className='h-96 w-full bg-background-primary mb-8'>
    
            </div>
            </>
          :<>
            <div className='pt-10'>
            <h2 className='animate-pulse mx-auto text-t-secondary text-4xl'>
              loading your data...
            </h2>
            </div>
          </>}
        </div>
      </section>
    </>
  )
}
