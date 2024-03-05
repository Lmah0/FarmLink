// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import ProfilePage from './jpComponents/ProfilePage';
import SignUpPage from './jpComponents/SignUpPage';
import LoginPage from './jpComponents/LoginPage';
import './App.css'; // Import the CSS file for styling

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <div className="nav-title">Make Agriculture Great Again</div>
          <ul className="nav-buttons">
            <li>
              <Link to="/profile">
                <button>Profile</button>
              </Link>
            </li>
            <li className="nav-right">
              <Link to="/signup">
                <button>Sign Up</button>
              </Link>
            </li>
            <li className="nav-right">
              <Link to="/login">
                <button>Login</button>
              </Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/signup" element={<SignUpPage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
