
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";

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
  const [userID, setUserID] = useState(false);

  const handleUserIdChange = (newUserId) => {
    setUserID(newUserId);
  };

  useEffect(() => {
    // This useEffect gets all the postings every time an event occurs on the page and stores them in items array
    const fetchData = async () => {
      try {
        let response = await fetch("http://127.0.0.1:5000/getPostings", {
          method: "GET",
        });

        if (response.ok) {
          let jsonRes = await response.json();
          console.log(jsonRes, "JSON RES");
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
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          {/* <Route path="/" element={<HomePageEmpty />} /> */}
          {/* <Route path="/login" element={<LoginPage />} /> */}
          {/* <Route path="/signup" element={<SignUpPage />} /> */}



          {/* <Route path="/" element={<SellItems/>} /> */}

          {items.length === 0 ? (
            <Route path="/" element={<HomePageEmpty />} />
          ) : (
            <Route path="/" element={<HomePage items={items} />} />
          )}

          {/* <Route path="/Cart" element={<Cart/>} />
          <Route path="/Payment" element={<Payment/>} /> */}


        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
