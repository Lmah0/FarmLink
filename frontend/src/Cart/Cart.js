import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import './Cart.css';

function Cart() {
  const[objects, setObjects] = useState([]);
  const[price, setPrice] = useState(0);

  const navigate = useNavigate();

  const goToPayment = () => {
    navigate("/Payment", { state: {totalPrice:price}});
  }

  const fetchDataForID = async (itemId) => {
    try {
      const response = await fetch("http://127.0.0.1:5007/getItem")
      const data = response.json();
      const jsonData = JSON.parse(data);
      retrieveObject(jsonData);
      console.log(`${itemId}`)
    } catch (error) {
      console.error(`error fetching data for ${itemId}`, error);
    }
  };

  const fetchCartData = async (userId) => {
    try {
      const response = await fetch("http://127.0.0.1:5008/returnCart");
      const data = await response.json();

      const parsedData = JSON.parse(data);
      const itemIDs = parsedData.map(entry => entry.itemId)

      itemIDs.forEach(itemId => {
        fetchDataForID(itemId);
      });
    } catch (error){
      console.error(`Error fetching data`, error);
    }
  }

  useEffect(() => {
    fetchCartData(1);
    // const jsonStr = "";

    // const parsedData = JSON.parse(jsonStr);

    // const itemIDs = parsedData.map(entry => entry.itemId)

    // itemIDs.forEach(itemId => {
    //   fetchDataForID(itemId);
    // });
    // setObjects(parsedData);
  }, []);

  useEffect(() => {
    objects.forEach(object => {
      setPrice(price + object.itemPrice);
    })
  }, [objects])
  
  const retrieveObject = (jsonData) => {
    const newObject = {
      userId: 1,
      itemId: jsonData.itemId, 
      itemName: jsonData.itemName,
      description: `This is Object ${objects.length + 1}`,
      postingAuthor: jsonData.postingAuthor,
      itemPrice: jsonData.itemPrice
    }
    setObjects([...objects, newObject])
  }
  

  const addObject = () => {
    const newObject = { 
      userId: 1,
      itemId: objects.length + 1, 
      itemName: `Object ${objects.length + 1}`,
      description: `This is Object ${objects.length + 1}`,
      postingAuthor: `The Owner is User1`,
      itemPrice: 39.99
      }
    setObjects([...objects, newObject]);
  };

  return (
    <div className="App">
      <div>
        <button onClick = {addObject}>Here is where the Entries will be</button>
        <h2 className="cart">Items in Cart</h2>
        <div>
          {objects.map(object => (
            <div key={object.itemId} className="List-Object">
              <div className="Object-Image"> Reserved Space</div>
              <div className="Object-Text">
                <button className="name-button" style={{margin:"5px"}}>{object.itemName}</button>
                <div style={{display: "flex", justifyContent: "space-between"}}>
                  <span style={{margin:"5px"}}>{object.description}</span>
                  <span style={{margin:"5px"}}>{object.postingAuthor}</span>
                </div>
                <span style={{margin:"5px", fontWeight:"bold"}}>{object.itemPrice}</span>
              </div>
            </div>
          ))}
        </div>
        <div style={{display: "flex", justifyContent: "space-between"}}>
          <span style={{marginLeft:"25px"}}>Price</span>
          <span style={{marginRight:"25px"}}>{price}</span>
        </div>
        <button style={{marginLeft:"25px", background:"transparent"}} onClick={goToPayment}>Pay Price</button>
      </div>
    </div>
  );
}

export default Cart;
