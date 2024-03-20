import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import './SignUpPage.css'; // Import the CSS file for styling

const SignUpPage = () => {
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState(''); // Updated to store role as a string
  const [farmerPid, setFarmerPid] = useState('');
  const [profileBio, setProfileBio] = useState('');

  const handleSignUp = async (e) => {
    e.preventDefault();

    try {
      // Make a POST request to your Flask API endpoint for user registration
      const response = await fetch('https://maga-user-management-7c1e7511f413.herokuapp.com/register', {
        method: 'POST',
        body: JSON.stringify({
          name: name,
          phone_number: phoneNumber,
          email_address: email,
          password: password,
          role: role, // Keep it as a string in the state
          farmer_pid: role === 'FARMER' ? parseInt(farmerPid) : 0, // Set PID to null if not a farmer
          profile_bio: profileBio,
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        // Handle successful sign-up
        alert('Sign up successful!');
        navigate("/login");
      } else {
        // Handle unsuccessful sign-up
        const data = await response.json();
        alert(`Sign up failed: ${data.message}`);
      }
    } catch (error) {
      console.error('Error during sign-up:', error);
      alert('Sign up failed. Please try again later.');
    }
  };

  return (
    <div className='signup-container'>
      <form className="signup-form" onSubmit={handleSignUp}>
        <div className="signup-fields">
          <h2 className="signup-title">Sign Up</h2>
          <div className='signup-form-group'>
            <label className="signup-label">Name</label>
            <input className="input-form" type="text" value={name} onChange={(e) => setName(e.target.value)} />
          </div>
          <div className='signup-form-group'>
            <label className="signup-label">Phone Number</label>
            <input className="input-form" type="text" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} />
          </div>
          <div className='signup-form-group'>
            <label className="signup-label">Email</label>
            <input className="input-form" type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
          </div>
          <div className='signup-form-group'>
            <label className="signup-label">Password</label>
            <input className="input-form" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </div>
          <div className='signup-form-group'>
            <label className="signup-label">Role</label>
            <select className="input-form" value={role} onChange={(e) => setRole(e.target.value)}>
              <option value="">Select Role</option>
              <option value="FARMER">Farmer</option>
              <option value="NONFARMER">Not a Farmer</option>
            </select>
          </div>
          {role === 'FARMER' && (
            <div className='signup-form-group'>
              <label className="signup-label">Farmer PID</label>
              <input type="text" value={farmerPid} onChange={(e) => setFarmerPid(e.target.value)} />
            </div>
          )}
          <div className='signup-form-group'>
            <label className="signup-label">Profile Bio</label>
            <input className="input-form" type="text" value={profileBio} onChange={(e) => setProfileBio(e.target.value)} />
          </div>
          <button id="signup-button" type="submit">Sign Up</button>
          </div>
      </form>
    </div>
  );
};

export default SignUpPage;
