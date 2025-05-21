import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {Routes, Route} from 'react-router-dom'
import Landing from './pages/Landing'
import Additional from './pages/Additional'
import Projects from './pages/Projects'
import Navbar from './components/Navbar'
import Logo from './components/Logo'

function App() {
  return (
    <div id='background'>
      <div className="corner top-left"></div>
      <div className="corner top-right"></div>
      <div className="corner bottom-left"></div>
      <div className="corner bottom-right"></div>

        <Navbar/>
        <Logo/>
        <Routes>
          <Route path='/' element={<Landing />} />
          <Route path='/projects' element={<Projects />} />
          <Route path='/additional' element={<Additional />} />
        </Routes>
        
    </div>
  )
}

export default App
