import "./HomePage.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import React from "react";

function HomePage({ items, loading, currentUserID, currentRole }) {
  const navigate = useNavigate();
  const [expandedBoxes, setExpandedBoxes] = useState(
    Array(items.length).fill(false)
  );
  const [expandedBoxIndex, setExpandedBoxIndex] = useState(null);
  const [yesExpandedBoxActive, setYesExpandedBoxActive] = useState(false);

  const handleExpandBox = (index) => {
    const newExpandedBoxes = [...expandedBoxes];
    newExpandedBoxes[index] = true;
    setExpandedBoxes(newExpandedBoxes);
    setYesExpandedBoxActive(true);
    setExpandedBoxIndex(index);
  };

  const handleUnexpandBox = () => {
    setExpandedBoxes(Array(items.length).fill(false));
    setYesExpandedBoxActive(false);
    setExpandedBoxIndex(null);
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
          // console.log(jsonRes, "JSON RES");
          alert("Added to cart!");
        } else {
          // console.log("Failed to fetch data:", response.status);
          alert("Failed to add to cart. Please try again later");
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    addToCart(itemId);
  };

  return (
    <>
      {loading ? (
        <div id="loading-message">Loading...</div>
      ) : (
        <div id="HomePage-Main-Container">
          <div id="HomePage-Header">
            <header>MarketPlace</header>
            <div id="HomePage-Buttons">
              <button
                id="HomePage-Header-SELL"
                onClick={handleSellItemClick}
                className={
                  currentRole === "FARMER" ? "sell-button" : "hidden-button"
                }
              >
                Sell
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
                  // currentUserID === item.user_id
                  //   ? "hidden-element" :
                    expandedBoxes[index]
                    ? "expanded-item-box"
                    : yesExpandedBoxActive === true &&
                      expandedBoxIndex !== index
                    ? "hidden-button"
                    : "item-box-not-expanded"
                }
                key={item.id}
              >
                <div
                  className={
                    expandedBoxes[index]
                      ? "expanded-img-wrapper"
                      : yesExpandedBoxActive === true &&
                        expandedBoxIndex !== index
                      ? "hidden-button"
                      : "button-img-wrapper"
                  }
                >
                  <img
                    id={
                      expandedBoxes[index]
                        ? "expanded-box-img"
                        : yesExpandedBoxActive === true &&
                          expandedBoxIndex !== index
                        ? "hidden-button"
                        : "Item-box-img"
                    }
                    src={`data:image/jpeg;base64,${item.image}`}
                    alt="Product item"
                    onClick={() => handleExpandBox(index)}
                  />
                </div>
                <p
                  className={
                    expandedBoxes[index] ? "post-attribute" : "hidden-element"
                  }
                >
                  <b>Seller:</b> {item.posting_author}
                </p>
                <p className="post-attribute">
                  <b>Name:</b>
                  <span>&nbsp;</span>
                  {item.posting_item["name"]}
                </p>
                <p className="post-attribute">
                  <b>Price:</b>
                  <span>&nbsp;</span>${item.posting_item["price"]}
                </p>
                <p
                  className={
                    expandedBoxes[index] ? "post-attribute" : "hidden-element"
                  }
                >
                  <b>Quantity Available:</b>
                  <span>&nbsp;</span>
                  {item.quantity}
                </p>
                <p
                  className={
                    expandedBoxes[index] ? "hidden-element" : "post-attribute"
                  }
                >
                  <b>Seller:</b>
                  <span>&nbsp;</span>
                  {item.posting_author}
                </p>
                <p
                  className={
                    expandedBoxes[index] ? "post-attribute" : "hidden-element"
                  }
                >
                  <b>Description:</b>
                  <span>&nbsp;</span>
                  {item.description}
                </p>
                <button
                  id="add-item-to-cart"
                  className={expandedBoxes[index] ? "" : "hidden-element"}
                  onClick={() => handleAddToCartClick(item.id)}
                >
                  Add to Cart
                </button>
                <button
                  id="close-posting"
                  className={expandedBoxes[index] ? "" : "hidden-element"}
                  onClick={() => handleUnexpandBox()}
                >
                  Close Listing
                </button>
              </div>
            ))}
          </div>
        </div>
      )}
    </>
  );
}

export default HomePage;
