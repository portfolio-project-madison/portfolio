import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {Routes, Route} from 'react-router-dom'
import Landing from './pages/Landing'
import Additional from './pages/Additional'
import Projects from './pages/Projects'
import Navbar from './components/Navbar'

function App() {
  return (
    <>
        <Navbar/>
        <Routes>
          <Route path='/' element={<Landing />} />
          <Route path='/projects' element={<Projects />} />
          <Route path='/additional' element={<Additional />} />
        </Routes>
    </>
  )
}

export default App
