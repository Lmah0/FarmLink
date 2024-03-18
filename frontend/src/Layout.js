import "./Layout.css";
import { Outlet } from "react-router-dom";
// import { useNavigate } from 'react-router-dom';


function Layout() {
    // const navigate = useNavigate();

    // const goToCart = () => {
    //     navigate("/Cart")
    // }

    return (
        <>
            <div id="Main-Container">
                <header>
                    Make Agriculture Great Again
                    {/* <button style={{marginRight: 20}} onClick={goToCart}>&#x1f6d2;</button> */}
                </header>

                <div>
                    <Outlet />
                </div>

                <footer>
                    &#169;MAGA
                </footer>
            </div>
        </>
    );
}
  
export default Layout;