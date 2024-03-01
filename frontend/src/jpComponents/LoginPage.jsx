// src/components/LoginPage.jsx
import React, { useState } from 'react';

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
  
    const handleLogin = (e) => {
      e.preventDefault();
  
      // Add your authentication logic here (e.g., API call, check credentials)
      // For simplicity, let's assume the login is successful if both fields are non-empty
      if (username && password) {
        alert('Login successful!');
        // You might also want to set some authentication state or redirect the user
      } else {
        alert('Please enter both username and password.');
      }
    };
  
    return (
      <div>
        <h2>Login Page</h2>
        <form onSubmit={handleLogin}>
          <label>
            Username:
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
          </label>
          <br />
          <label>
            Password:
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </label>
          <br />
          <button type="submit">Login</button>
        </form>
      </div>
    );
  
};

export default LoginPage;
