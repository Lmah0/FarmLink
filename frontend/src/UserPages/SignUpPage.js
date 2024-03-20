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
      const response = await fetch('http://127.0.0.1:5000/register', {
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
      <form onSubmit={handleSignUp}>
        <h2>Sign Up Page</h2>
        <div className='form-group'>
          <label>Name</label>
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        </div>
        <div className='form-group'>
          <label>Phone Number</label>
          <input type="text" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} />
        </div>
        <div className='form-group'>
          <label>Email</label>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </div>
        <div className='form-group'>
          <label>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <div className='form-group'>
          <label>Role</label>
          <select value={role} onChange={(e) => setRole(e.target.value)}>
            <option value="">Select Role</option>
            <option value="FARMER">Farmer</option>
            <option value="NONFARMER">Not a Farmer</option>
          </select>
        </div>
        {role === 'FARMER' && (
          <div className='form-group'>
            <label>Farmer PID</label>
            <input type="text" value={farmerPid} onChange={(e) => setFarmerPid(e.target.value)} />
          </div>
        )}
        <div className='form-group'>
          <label>Profile Bio</label>
          <input type="text" value={profileBio} onChange={(e) => setProfileBio(e.target.value)} />
        </div>
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
};

export default SignUpPage;
