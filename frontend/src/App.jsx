import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'

import { Error } from './components/Error'
import { Landing } from './components/Landing'
import { NoAuth } from './components/NoAuth'
import { Temp } from './components/Temp'
import { Auth } from './components/Auth'
import { User } from './components/User'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" index element={<Landing/>}/> <Route path="/home" element={<Navigate to="/" replace/>}/> <Route path="/index" element={<Navigate to="/" replace/>}/>
        <Route path="auth" element={<Auth/>}/>
        <Route path="noauth" element={<NoAuth/>}/>
        {/* <Route path="temp" element={<Temp/>}/> */}
        <Route path="user" element={<User />}/>
        <Route path="*" element={<Error/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App
