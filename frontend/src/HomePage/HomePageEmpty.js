import "./HomePageEmpty.css";
import { useNavigate } from "react-router-dom";
import { Typed } from "react-typed";
import React from "react";
import logo from "./../Images/agriculture.png";


function HomePageEmpty() {
  const navigate = useNavigate();

  const handleSignUpClick = () => {
    navigate("/signup");
  };

  const handleLoginClick = () => {
    navigate("/login");
  };

  const el = React.useRef(null);
  
  React.useEffect(() => {
      const typed = new Typed(el.current, {
          strings: ["Branching the agricultural market starts here."],
          typeSpeed: 50,
      });
      
      return () => {
          // Destroy Typed instance during cleanup to stop animation
          typed.destroy();
      };

  }, []);

  return (
    <div>
      <div id="HomePage-Main-Container">
        <div className="login-page">
          <div className="motto typewriter">
            <h1><span ref={el} /></h1>
          </div>
          <div className="auth-buttons">
            <button className="auth-button" onClick={handleSignUpClick}>
              Sign Up
            </button>
            <br />
            <button className="auth-button" onClick={handleLoginClick}>
              Login
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomePageEmpty;
