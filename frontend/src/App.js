// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import PaymentPage from './jpComponents/PaymentPage';
import SignUpPage from './jpComponents/SignUpPage';
import LoginPage from './jpComponents/LoginPage';
import './App.css'; // Import the CSS file for styling

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul className="nav-buttons"> {/* Add a class for styling */}
            <li>
              <Link to="/payment">
                <button>Payment</button>
              </Link>
            </li>
            <li>
              <Link to="/signup">
                <button>Sign Up</button>
              </Link>
            </li>
            <li>
              <Link to="/login">
                <button>Login</button>
              </Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/payment" element={<PaymentPage />} />
          <Route path="/signup" element={<SignUpPage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
