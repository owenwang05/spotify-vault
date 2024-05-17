import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { Error } from './components/Error'
import { Landing } from './components/Landing'
import { Footer } from './components/Footer'

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" index element={<Landing/>}/>
        <Route path="/home" element={<Navigate to="/" replace/>}/>
        <Route path="/index" element={<Navigate to="/" replace/>}/>
        <Route path="*" element={<Error/>}/>
      </Routes>
      <Footer/>
    </BrowserRouter>
  );
}

export default App
