
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import HomePageEmpty from "./HomePage/HomePageEmpty";
import HomePage from "./HomePage/HomePage";
import Cart from "./Cart/Cart";
import Payment from "./Payment/Payment";
import Layout from "./Layout";

function App() {
  /* This is the main app component basically the "view controller" this will just pass information along to different pages from API */

  const [items, setItems] = useState([]);

  useEffect(() => {
    // This gets all the postings every time the page an event occurs and stores them in items array
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

          {items.length === 0 ? (
            <Route path="/" element={<HomePageEmpty />} />
          ) : (
            <Route path="/" element={<HomePage items={items} />} />
          )}
          <Route path="/Cart" element={<Cart/>} />
          <Route path="/Payment" element={<Payment/>} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
