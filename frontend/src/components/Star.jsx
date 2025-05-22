export default function Star({ className = '' }){
  return(
    <>
    <div className={`star ${className}`}>
           <svg width="60" height="60" viewBox="0 0 100 100"> {/*star*/}
          <polygon 
            points="50,5 61,35 95,35 67,57 78,91 50,70 22,91 33,57 5,35 39,35" 
            fill="#8F5E72" 
            stroke="black" 
            strokeWidth="4" 
            strokeLinejoin="round"
          />
        </svg>
        </div>
    </>
  )
}