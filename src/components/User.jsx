import { UserHeader } from './Header'
import { getTopArtists, getTopSongs } from '../data_access'

export function User(){

  const profile = JSON.parse(localStorage.getItem("profile"));

  const topArtists = JSON.parse(localStorage.getItem("topSongs"));
  const topSongs = JSON.parse(localStorage.getItem("topArtists"));

  console.log(topSongs);

  for(var i = 0; i < topSongs.items.length; i++) {
    console.log(i);
  }

  return (
    <>
      <UserHeader />
      <section className="w-full h-full bg-background-secondary">
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
  
          <div className="grid grid-cols-3 gap-8 w-full">
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
        </div>
      </section>
    </>
  )
}
