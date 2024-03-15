import React, { useEffect, useState } from 'react';
import './ProfilePage.css'; // Import the CSS file for styling

const ProfilePage = () => {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    // Fetch user profile data from localStorage
    const profileData = JSON.parse(localStorage.getItem('profile'));
    if (profileData) {
      setUserData(profileData);
    }
  }, []);

  return (
    <div className="profile-container">
      <h2>Profile Page</h2>
      {userData ? (
        <div className="profile-details">
          <p><strong>Name:</strong> {userData.name}</p>
          <p><strong>Email:</strong> {userData.email_address}</p>
          <p><strong>Phone:</strong> {userData.phone_number}</p>
          <p><strong>Role:</strong> {userData.role}</p>
          <p><strong>PID:</strong> {userData.farmer_pid}</p>
          <p><strong>Profile Bio:</strong> {userData.profile_bio}</p>

        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default ProfilePage;
