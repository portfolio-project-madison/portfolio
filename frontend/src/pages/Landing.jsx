import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import '../styles/landing-styles.css'

export default function Landing(){
  const [error, setError] = useState('')
  const [socials, setSocials] = useState([])
  const [competencies, setCompetencies] = useState([])
  const [bio, setBio] = useState('')
////socials////
  useEffect(() => {
    const fetchSocials = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/info/social`, {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json", // We're telling the server we expect JSON
          }
        });
        setSocials(response.data)
        
        } catch (err) {
          setError(err.message);
        }
    };
    fetchSocials();
  }, []);

////competencies////
  useEffect(() => {
    const fetchCompetencies = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/info/tech-competencies`, {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json", // We're telling the server we expect JSON
          }
        });
        setCompetencies(response.data)
      
        } catch (err) {
          setError(err.message);
        }
      };
    fetchCompetencies();
  }, []);

////bio////
  useEffect(() => {
    const fetchBio = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/info/bio`, {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json", // We're telling the server we expect JSON
          }
         
        }); 
        setBio(response.data[0])
      
        } catch (err) {
          setError(err.message);
        }
      };
    fetchBio();
  }, []);

  return (
  <div id='info-wrapper'>
  {/* socials */}
    <ul className='socials_container'>
      {socials.length > 0 ? (
        socials.map((social) => <li className='social_container'key={social.title}>{
          <div className='social'>
            <p className="square"> oh</p>
            <a href={social.link} className='social-info'>{social.title}</a>
          </div>
        }</li>)
      ) : (
        <p className="emptyMessage" >can't get socials :/</p>
      )}
    </ul>
  {/* bio */}
      <div id='bio-container'>
        <h1 id="bio-title"> about me!</h1>
        <p id='bio'>{bio.bio}</p>
        <div className="star" id='1'>
           <svg width="60" height="60" viewBox="0 0 100 100"> {/*star*/}
          <polygon 
            points="50,5 61,35 95,35 67,57 78,91 50,70 22,91 33,57 5,35 39,35" 
            fill="#8F5E72" 
            stroke="black" 
            stroke-width="4" 
            stroke-linejoin="round"
            transform="rotate(30 50 50)" 
          />
        </svg>
        </div>
       
      </div>
  {/* competencies */}
 
  <ul className='competencies_container'> 
    <h1 id='tech-title'> technical competencies!</h1>
      {competencies.length > 0 ? 
        Object.entries(
          competencies.reduce((acc, competency) => {
            const {type,title} = competency
            if(!acc[type]) acc[type] = []
            acc[type].push(title)
            return acc
          }, {}))
          .map(([type,titles]) => (
            <div className="competency-container">
              <p className='competency_line' key={type}>
              <strong>{type}:</strong> {titles.join(', ')}
            </p>
            </div>
          )
      ) : (
          <p className="emptyMessage" >can't get competencies :/</p>
      )}
  </ul>
  </div>
  )
}