import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import '../styles/additional-styles.css'
import Star from '../components/Star'

export default function Additional(){
  const [error,setError] = useState('')
  const [projects,setProjects] = useState([])

  ////projects////
  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await axios.get(`/info/additional-projects`, {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json", // We're telling the server we expect JSON
          }
        });
        setProjects(response.data)
        
        } catch (err) {
          setError(err.message);
        }
    };
    fetchProjects();
  }, []);


  return (
  <>
    {/* projects */}
    <ul className='projects-container'>
      {projects.length > 0 ? (
        projects.filter(project => project.type === 'ai').map((project) => <li className='project-container'key={project.title}>{
          <div className='project'>
            <Star className='two'/>
            <Star className='three'/>
            <img src={project.link} className='project-img' alt="project"/>
            <Star className='four'/>
            <Star className='twotwo'/>
            <Star className='five'/>
            <div id='project-info'>
              <p className="project-title">{project.title}!</p>
              <p className="project-bio">{project.bio}</p>
            </div> 
          </div>
        }</li>)
      ) : (
        <p className="emptyMessage" >can't get projects :/</p>
      )}
      {projects.length > 0 ? (
        <div id='yt-box'>
          <img src={projects[projects.length-1].img} id="yt-img" alt="yt-project"/>
          <div id="yt-text-column">
            <a href={projects[projects.length-1].link} id="yt-text"> youtube! </a>
            <p>{projects[projects.length-1].bio}</p>
          </div>

        </div>
      ) : (
        <p className="emptyMessage" >can't get youtube :/</p>
      )}
    </ul>
  
  </>
)}