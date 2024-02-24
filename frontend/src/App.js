
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePageEmpty from "./HomePage/HomePageEmpty";
import HomePage from "./HomePage/HomePage";
import Layout from "./Layout";



function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          /* This is the default route, users will be asked to login/signup first then it 
             will check backend for listings and determine which page to switch to */
              
          {/* <Route path="/" element={<LoginSignUpPage />} /> */} 

          <Route path="/EmptyListings" element={<HomePageEmpty />} />
          <Route path="/Listings" element={<HomePage />} />
          <Route path="*" element={<h1>Not Found</h1>} />

        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;

