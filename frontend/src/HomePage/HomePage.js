import "./HomePage.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function HomePage({ items, handleLogout, currentUserID, currentRole }) {
  const navigate = useNavigate();
  const [expandedBoxes, setExpandedBoxes] = useState(
    Array(items.length).fill(false)
  );
  const [expandedBoxIndex, setExpandedBoxIndex] = useState(null);
  const [yesExpandedBoxActive, setYesExpandedBoxActive] = useState(false);

  const handleBoxClick = (index) => {
    const newExpandedBoxes = [...expandedBoxes];
    newExpandedBoxes[index] = !newExpandedBoxes[index];
    setExpandedBoxes(newExpandedBoxes);
    setYesExpandedBoxActive(!yesExpandedBoxActive);
    if (expandedBoxIndex !== null) {
      setExpandedBoxIndex(null);
    } else {
      setExpandedBoxIndex(index);
    }
  };

  const goToCart = () => {
    navigate("/Cart");
  };

  const goToProfile = () => {
    navigate("/profile");
  };

  const handleLogoutClick = () => {
    handleLogout();
  };

  const handleSellItemClick = () => {
    navigate("/SellItems");
  };

  const handleAddToCartClick = (itemId) => {
    const addToCart = async (itemId) => {
      // This function will flush the cart when the user logs out
      try {
        let response = await fetch("http://127.0.0.1:5008/addToCart", {
          method: "POST",
          body: JSON.stringify({
            userId: currentUserID,
            itemId: itemId,
            quantity: 1,
          }),
          headers: {
            "Content-Type": "application/json",
          },
        });
        if (response.ok) {
          let jsonRes = await response.json();
          console.log(jsonRes, "JSON RES");
        } else {
          console.log("Failed to fetch data:", response.status);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    addToCart(itemId);
  };

  return ( 
    <>
      <div id="HomePage-Main-Container">
        <div id="HomePage-Header">
          <header>MarketPlace</header>
          <div id="HomePage-Buttons">
            <button
              id="HomePage-Header-SELL"
              onClick={handleSellItemClick}
              className={currentRole === "FARMER" ? "" : "hidden-button"}
            >
              Sell Item
            </button>
          </div>
        </div>

        <div
          id="main-ItemBox-container"
          className={
            expandedBoxes.includes(true) ? "expanded-main-container" : ""
          }
        >
          {items.map((item, index) => (
            <div
              id="Item-box"
              className={
                expandedBoxes[index] ? "expanded-item-box" :
                (yesExpandedBoxActive === true && expandedBoxIndex !== index ? "hidden-button" : "")
              }
              key={item.id}
            >
              <div id="button-img-wrapper">
                <img
                  id="Item-box-img"
                  src={`data:image/jpeg;base64,${item.image}`}
                  alt="Product item"
                  onClick={() => handleBoxClick(index)}
                  />
                <button
                  id="add-item-to-cart"
                  className={expandedBoxes[index] ? "" : "hidden-element"}
                  onClick={() => handleAddToCartClick(item.id)}
                >
                  <img
                    src="https://static-00.iconduck.com/assets.00/sign-plus-icon-2048x2047-jdkmk1r1.png"
                    alt="Plus-Icon"
                  />
                </button>
              </div>
              <h4 className={expandedBoxes[index] ? "" : "hidden-element"}>
                Seller: {item.posting_author}
              </h4>
              <h3>{item.posting_item["name"]}</h3>
              <h4>Price: ${item.posting_item["price"]}</h4>
              <h4 className={expandedBoxes[index] ? "" : "hidden-element"}>
                Quantity Available: {item.quantity}
              </h4>
              <h4 className={expandedBoxes[index] ? "hidden-element" : ""}>
                Seller: {item.posting_author}
              </h4>
              <p className={expandedBoxes[index] ? "" : "hidden-element"}>
                Description: {item.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default HomePage;
