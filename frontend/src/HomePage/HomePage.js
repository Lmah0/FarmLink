import "./HomePage.css";
import { useState } from "react";

function HomePage({ items }) {
  const [expandedBox, setExpandedBox] = useState(null);

  const handleBoxClick = () => {
    if (expandedBox === 0) {
      setExpandedBox(null);
    } else {
      setExpandedBox(0);
    }
  };

  return (
    <>
      <div id="HomePage-Main-Container">
        <div id="HomePage-Header">
          <header>MarketPlace</header>
          <input type="text" placeholder="Search" />
          <button id="search-Button">
            <img
              src="https://media.istockphoto.com/id/1131164548/vector/avatar-5.jpg?s=612x612&w=0&k=20&c=CK49ShLJwDxE4kiroCR42kimTuuhvuo2FH5y_6aSgEo="
              alt="Person Emoji"
            />
          </button>
        </div>

        <div
          id="main-ItemBox-container"
          className={expandedBox === 0 ? "expanded-main-container" : ""}
        >
          {items.map((item, index) => (
            <div
              id="Item-box"
              className={expandedBox === 0 ? "expanded-item-box" : ""}
              key={item.id}
            >
              <div id={expandedBox === 0 ? "button-img-wrapper" : ""}>
                <img
                  id="Item-box-img"
                  src="https://cdn.britannica.com/22/215522-050-8315BB78/green-grass-close-up.jpg"
                  alt="Product item"
                  onClick={handleBoxClick}
                />

                <button
                  id="add-item-to-cart"
                  className={expandedBox === 0 ? "" : "hidden-element"}
                >
                  <img
                    src="https://static-00.iconduck.com/assets.00/sign-plus-icon-2048x2047-jdkmk1r1.png"
                    alt="Plus-Icon"
                  />
                </button>
              </div>
              
              <h4 className={expandedBox === 0 ? "" : "hidden-element"}>Seller: {item.posting_author}</h4>

              <h3>{item.posting_item['name']}</h3>

              <h4>Price: ${item.posting_item['price']}</h4>

              <h4 className={expandedBox === 0 ? "" : "hidden-element"}>
                Quanity Avaliable: {item.quantity}
              </h4> 
                
              <h4 className={expandedBox === 0 ? "hidden-element" : ""}>Seller: {item.posting_author}</h4>

              <p className={expandedBox === 0 ? "" : "hidden-element"}>
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
