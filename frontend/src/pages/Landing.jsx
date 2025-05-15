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
  <>
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
        <p id='bio'>{bio.bio}</p>
      </div>
  {/* competencies */}
  <ul className='competencies_container'>
      {competencies.length > 0 ? (
        competencies.map((competency) => <li className='competency_container'key={competency.title}>{
          <div className='competency'>
            <p className='competency-info'>{competency.type}: {competency.title}</p>
          </div>
        }</li>)
      ) : (
        <p className="emptyMessage" >can't get competencies :/</p>
      )}
    </ul>
  </>
  )
}