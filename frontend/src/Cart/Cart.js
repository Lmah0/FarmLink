import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import './Cart.css';

function Cart() {
  const[objects, setObjects] = useState([]);
  const[totPrice, setTotPrice] = useState(0);

  const navigate = useNavigate();

  const goToPayment = () => {
    navigate("/Payment", { state: {totalPrice:totPrice}});
  }

  const fetchDataForID = async (itemID) => {
    try {
      const response = await fetch("http://127.0.0.1:5007/getItem", {
        method: "POST",
        body: JSON.stringify({
          itemId: itemID
        }),
        headers: {
          'Content-Type' : 'application/json',
        },
      });
      if (response.ok) {
        const data = await response.json();
        console.log(data, "JSON RES");
        // const parsedData = JSON.parse(data);
        console.log(`${data.item_type}`)
        // let jsonRes = await response.json();
        retrieveObject(data);
        
      } else {
        console.log("Failed to fetch data:", response.status);
      }
      // const data = response.json();
      // const jsonData = JSON.parse(data);
      // retrieveObject(jsonData);

    } catch (error) {
      console.error(`error fetching data for ${itemID}`, error);
    }
  };

  const fetchCartData = async (useId) => {
    try {
      const response = await fetch(`http://127.0.0.1:5008/returnCart`, {
        method: "POST",
        body: JSON.stringify({
          userId: useId
        }),
        headers: {
          'Content-Type' : 'application/json',
        },
      });
      if (response.ok) {
        const data = await response.json();
        console.log(data, "JSON RES");
        // const parsedData = JSON.parse(data);
        const itemIDs = data.map(entry => entry.itemId)
  
        itemIDs.forEach(itemId => {
          fetchDataForID(itemId);
        });
        console.log(`Fetch cart data was run`);
        // let jsonRes = await response.json();
        
      } else {
        console.log("Failed to fetch data:", response.status);
      }

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
    let totalPrice = 0;
    objects.forEach(object => {
      totalPrice += object.price;
    });
    setTotPrice(totalPrice);
  }, [objects])
  
  const retrieveObject = (jsonData) => {
    const newObject = {
      userId: 1,
      itemId: jsonData.id, 
      item_type: jsonData.item_type,
      name: jsonData.name,
      posting_id: jsonData.posting_id,      // description: `This is Object ${objects.length + 1}`,
      // postingAuthor: jsonData.postingAuthor,
      price: jsonData.price
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
                <button className="name-button" style={{margin:"5px"}}>{object.name}</button>
                <div style={{display: "flex", justifyContent: "space-between"}}>
                  <span style={{margin:"5px"}}>Posting ID: {object.posting_id}</span>
                  <span style={{margin:"5px"}}>Item Type: {object.item_type}</span>
                </div>
                <span style={{margin:"5px", fontWeight:"bold"}}>Price: ${object.price}</span>
              </div>
            </div>
          ))}
        </div>
        <div style={{display: "flex", justifyContent: "space-between"}}>
          <span style={{marginLeft:"25px"}}>Price</span>
          <span style={{marginRight:"25px"}}>Total Price: ${totPrice}</span>
        </div>
        <button style={{marginLeft:"25px", background:"transparent"}} onClick={goToPayment}>Pay Price</button>
      </div>
    </div>
  );
}

export default Cart;
