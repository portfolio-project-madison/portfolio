import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import '../styles/project-styles.css'
import Star from '../components/Star'

export default function Projects(){
  const [error,setError] = useState('')
  const [techProjects,setTechProjects] = useState([])

  ////tech projects////
  useEffect(() => {
    const fetchTechProjects = async () => {
      try {
        const response = await axios.get(`/info/software-projects`, {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json", // We're telling the server we expect JSON
          }
        });
        setTechProjects(response.data)
        
        } catch (err) {
          setError(err.message);
        }
    };
    fetchTechProjects();
  }, []);

  return (
  <>
    {/* software projects */}
    <ul className='tech-projects-container'>
      {techProjects.length > 0 ? (
        techProjects.map((techProject) => <li className='tech-project-container'key={techProjects.title}>{
          <div className='tech-project'>
            <Star className="ten"/>
            <Star className="nine"/>
            <img src={techProject.img} className="tech-img" id={techProject.title}/>
            <div id="project-column">
              <a href={techProject.link} className='tech-project-title'>{techProject.title}</a>
              <p className="tech-project-bio" >{techProject.bio}</p>
            </div>
          </div>
        }</li>)
      ) : (
        <p className="emptyMessage" >can't get tech projects :/</p>
      )}
    </ul>
  
  </>
)}