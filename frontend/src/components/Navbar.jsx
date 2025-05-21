import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

export default function Navbar(){

  return(
  <div id = 'navbar'>
    <div id='nav-items'> 
      <Link to="/" className ='nav-item' >Home</Link> 
      <Link to="/additional" className ='nav-item' >Additional</Link> 
      <Link to="/projects" className ='nav-item' >Projects</Link> 
    </div>
  </div>
)}