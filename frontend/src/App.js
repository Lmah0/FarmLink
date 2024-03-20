
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";


import Layout from "./Layout";
import HomePageEmpty from "./HomePage/HomePageEmpty";
import HomePage from "./HomePage/HomePage";
import Cart from "./Cart/Cart";
import Payment from "./Payment/Payment";
import SellItems from "./SellItems/SellItems";
import LoginPage from "./UserPages/LoginPage";
import SignUpPage from "./UserPages/SignUpPage";
import ProfilePage from "./UserPages/ProfilePage";

function App() {
  /* This is the main app component basically the "view controller" this will just pass information along to different pages from API */

  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  const [userProfile, setUserProfile] = useState(
    JSON.parse(localStorage.getItem("profile"))
  );
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  const handleSetProfile = (userData) => {
    localStorage.setItem("profile", userData);
    const profileData = JSON.parse(localStorage.getItem('profile'));
    if (profileData) {
      setUserProfile(profileData);
    }
  };

  useEffect(() => {
    if (userProfile) {
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  });

  const handleLogout = () => {
    localStorage.removeItem("profile");
    setUserProfile(null);
  };


  useEffect(() => {
    // This useEffect gets all the postings every time an event occurs on the page and stores them in items array
    const fetchData = async () => {
      try {
        let response = await fetch("http://127.0.0.1:5007/getPostings", {
          method: "GET",
        });

        if (response.ok) {
          let jsonRes = await response.json();
          setLoading(false);
          // console.log(jsonRes);
          setItems(jsonRes);
        } else {
          console.log("Failed to fetch data:", response.status);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route element={<Layout handleLogout={handleLogout} isLoggedIn={isLoggedIn}/>}>

            { 
              userProfile ? (
                <>
                  <Route path="/" element={<HomePage items={items} loading={loading} currentUserID={userProfile.id} currentRole={userProfile.role} currentUserName={userProfile.name} /> } />
                  <Route path="/cart" element={<Cart currentUserID={userProfile.id} />} />
                  <Route path="/Payment" element={<Payment currentUserID={userProfile.id}/>} />
                  <Route path="/SellItems" element={<SellItems currentUserID={userProfile.id} currentUserName={userProfile.name}/>} />
                </>
              ) : (
                <Route path="/" element={<HomePageEmpty />} /> 
              )
            }

            <Route path="/login" element={<LoginPage handleSetProfile={handleSetProfile}/>} /> 
            <Route path="/signup" element={<SignUpPage />} />
            <Route path="/profile" element={<ProfilePage/>} />

          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
};

export default App;
