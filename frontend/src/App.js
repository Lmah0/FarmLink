
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePageEmpty from "./HomePageEmpty";
import HomePage from "./HomePage";
import Layout from "./Layout";

/* Will neeed to check the state of selling items to determine if its empty or not */

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<HomePageEmpty />} />
          <Route path="/Listings" element={<HomePage />} />
          <Route path="*" element={<h1>Not Found</h1>} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

