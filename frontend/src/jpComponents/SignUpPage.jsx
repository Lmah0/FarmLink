// src/components/SignUpPage.jsx
import React, { useState } from 'react';

const SignUpPage = () => {

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [pid, setPID] = useState('');
  
    const handleSignUp = (e) => {
      e.preventDefault();
  
      // Add your sign-up logic here (e.g., API call, validation)
      // For simplicity, let's assume the sign-up is successful if all fields are non-empty
      if (firstName && lastName && email && password && pid) {
        alert('Sign up successful!');
        // You might also want to redirect the user or set some state
      } else {
        alert('Please fill in all fields.');
      }
    };
  
    return (
      <div>
        <h2>Sign Up Page</h2>
        <form onSubmit={handleSignUp}>
          <label>
            First Name:
            <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
          </label>
          <br />
          <label>
            Last Name:
            <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} />
          </label>
          <br />
          <label>
            Email:
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
          </label>
          <br />
          <label>
            Password:
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </label>
          <br />
          <label>
            PID:
            <input type="text" value={pid} onChange={(e) => setPID(e.target.value)} />
          </label>
          <br />
          <button type="submit">Sign Up</button>
        </form>
      </div>
      );
    };

export default SignUpPage;
