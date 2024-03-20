import "./HomePageEmpty.css";
import { useNavigate } from "react-router-dom";
import React from "react";
function HomePageEmpty() {
  const navigate = useNavigate();

  const handleSignUpClick = () => {
    navigate("/signup");
  };

  const handleLoginClick = () => {
    navigate("/login");
  };

  return (
    <>
      <div id="HomePage-Main-Container">
        <div id="empty-holder">No Postings Currently Available</div>
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
    </>
  );
}

export default HomePageEmpty;
