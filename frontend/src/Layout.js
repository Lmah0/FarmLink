
import "./Layout.css";
import { Outlet } from "react-router-dom";

function Layout() {

    return (
        <>
            <div id="Main-Container">
                <header>Make Agriculture Great Again</header>

                <div>
                    <Outlet />
                </div>

                <footer>&#169;MAGA</footer>
            </div>
        </>
    );
}
  
export default Layout;