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
      {userData ? (
        <div className="profile-details">
          <h2>Profile Page</h2>
          <p className="profile-entry"><strong>Name:</strong> {userData.name}</p>
          <p className="profile-entry"><strong>I am:</strong> {userData.role === 'FARMER' ? "a farmer" : "not a farmer"}</p>
          <p className="profile-entry"><strong>Email:</strong> {userData.email_address}</p>
          <p className="profile-entry"><strong>Phone:</strong> {userData.phone_number}</p>
          {userData.role === 'FARMER' && (
            <p className="profile-entry"><strong>PID:</strong> {userData.farmer_pid}</p>
          )}
          <p className="profile-entry"><strong>Profile Bio:</strong> {userData.profile_bio}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default ProfilePage;
