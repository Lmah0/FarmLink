import "./HomePageEmpty.css";
import { useNavigate } from "react-router-dom";

function HomePageEmpty() {
  const navigate = useNavigate();

  const handleSignUpClick = () => {
    navigate("/signup");
  };

  const handleLoginClick = () => {
    navigate("/login");
  };

  return (
    <div>
      <div id="HomePage-Main-Container">
        <div className="login-page">
          <div>
            The path to branching the agricultural market starts here.
          </div>
          <div>
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
