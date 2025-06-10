import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import '../styles/landing-styles.css'
import Star from '../components/Star'

export default function Landing(){
  const [error, setError] = useState('')
  const [socials, setSocials] = useState([])
  const [competencies, setCompetencies] = useState([])
  const [bio, setBio] = useState([])
////socials////
  useEffect(() => {
    const fetchSocials = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5001/info/social`, {
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
        const response = await axios.get(`http://127.0.0.1:5001/info/tech-competencies`, {
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
        const response = await axios.get(`http://127.0.0.1:5001/info/bio`, {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json", // We're telling the server we expect JSON
          }
         
        }); 
        setBio(response.data)
      
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
            <img src={social.img} className="square"/>
            <a href={social.title.toLowerCase() === 'email' ? `mailto:${social.link}` : social.link} className='social-info'>{social.title}</a>
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
        <Star className='one'/>
      </div>

  {/* me */}
      <div id='me-container'>
        <img src={bio.img} id="me-img"/>
        <div id='me-text-container'>
          <p id="me-text">software engineer!</p>
        </div>
      </div>
  {/* competencies */}
  <div className='competencies_container'> 
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
            <div className="competency_container">
              <p className='competency_line' key={type}>
              <strong>{type}:</strong> {titles.join(', ')}
            </p>
            </div>
          )
      ) : (
          <p className="emptyMessage" >can't get competencies :/</p>
      )}
  </div>
  </div>
  )
}