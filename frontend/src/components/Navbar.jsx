import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

export default function Landing(){

  return(
  <>
      <Link to="/">Home</Link> |{" "}
      <Link to="/additional">Additional</Link> |{" "}
      <Link to="/projects">Projects</Link> 
      
  </>
)}