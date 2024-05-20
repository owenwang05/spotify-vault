import { useState, useEffect } from 'react';

import { UserHeader } from './Header'
import { checkValidSession, getProfile, getTopSongs, getTopArtists, getListenTime, getTopGenres } from '../data_access'
import { clearData, checkAPICode } from '../auth';

export function User(){
  const [profile, setProfile] = useState(undefined);
  const [listenTime, setListenTime] = useState(undefined);
  const [topGenres, serToGenres] = useState(undefined); 
  const [topArtists, setArtists] = useState(undefined);
  const [topSongs, setSongs] = useState(undefined);

  useEffect(() => {(async () => {
    await checkValidSession(); 
    try {
      getProfile(setProfile);
      getListenTime(setListenTime);
      getTopArtists(setArtists);
      getTopSongs(setSongs); 
    } catch(e) {
      console.error(e);
    }
  })();}, []);

  return (
    <>
      <UserHeader />
      <section className="w-full h-full min-h-screen px-6 bg-background-secondary">
        <div className='flex flex-col gap-4 justify-center items-center max-w-6xl mx-auto'>
          {profile ?
            <div className="animate-loadIn flex flex-row items-center justify-start gap-12 w-full">
              <img 
                alt="profile picture"
                src={profile.images[1].url}
                className='w-75 rounded-full'
              />
              <h1 className="text-t-primary text-7xl font-medium font-akshar">
                {profile.display_name}
              </h1>
            </div>
            : 
            <></>
          }
          {topSongs && topArtists && listenTime
          ?
            <>
              <div className="animate-loadIn grid grid-cols-3 gap-4 w-full">
                
                <div className="h-full bg-background-primary text-t-primary rounded-lg">
                  <div className='p-6'>
                    <h1 className='text-3xl font-semibold'>Listening Time</h1>
                    <div className="text-5xl font-semibold my-6">
                      <span>{(Math.floor((listenTime / 3600000) % 24))}h{' '}</span>
                      <span>{("0" + Math.floor((listenTime / 60000) % 60)).slice(-2)}m{' '}</span>
                      <span>{("0" + Math.floor((listenTime / 1000) % 60)).slice(-2)}s</span>
                    </div>
                    <h1 className='text-3xl font-semibold'>Top Genres</h1>
                  </div>
                </div>
                <div className="h-full bg-background-primary text-t-primary rounded-lg">
                  <div className='p-6 flex flex-col gap-4'>
                    <h1 className='text-3xl font-semibold'>Top Songs</h1>
                    {topSongs.items.map((item, index) => (
                      <div key={index} className='flex flex-row items-center gap-4'>
                        <img 
                          alt="top artists" 
                          src={item.album.images[0].url} 
                          className='w-16 rounded-full'
                        />
                        <div className="flex flex-col w-full overflow-hidden">
                          <h2 className='text-lg font-semibold text-t-primary truncate w-11/12'>{item.name}</h2>
                          <h3 className='text-base text-t-secondary truncate w-11/12'>
                            {item.artists[0].name}
                          </h3>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="h-full bg-background-primary text-t-primary rounded-lg">
                  <div className='p-6 flex flex-col gap-4'>
                    <h1 className='text-3xl font-semibold'>Top Artists</h1>
                    {topArtists.items.map((item, index) => (
                      <div key={index} className='flex flex-row items-center gap-4'>
                      <img 
                        alt="top artists" 
                        src={item.images[0].url} 
                        className='w-16 rounded-full'
                      />
                      <div className="flex flex-col w-full overflow-hidden">
                        <h2 className='text-lg font-semibold text-t-primary truncate w-11/12'>{item.name}</h2>
                      </div>
                    </div>
                    ))}
                  </div>
                </div>
              </div>
      
              <div className='animate-loadIn h-96 w-full bg-background-primary'>
                
              </div>
      
              <div className='animate-loadIn h-96 w-full bg-background-primary mb-8'>
      
              </div>
            </>
          :
            <>
              <div className='flex flex-col justify-center align-middle h-full pt-40'>
                <h1 className='animate-pulse mx-auto text-t-secondary text-4xl'>
                  loading your data...
                </h1>
              </div>
            </>
          }
        </div>
      </section>
    </>
  )
}
