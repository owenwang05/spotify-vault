import { BrowserRouter, Routes, Route, redirect } from 'react-router-dom'
import { Error } from './components/Error'
import { Index } from './components/Index'
import { Footer } from './components/Footer'
import { Header } from './components/Header'

function App() {

  return (
    <BrowserRouter>
      <Header/>
      <Routes>
        <Route path="/" index element={<Index/>}/>
        <Route path="/home" element={redirect("/")}/>
        <Route path="*" element={<Error/>}/>
      </Routes>
      <Footer/>
    </BrowserRouter>
  )
}

export default App
