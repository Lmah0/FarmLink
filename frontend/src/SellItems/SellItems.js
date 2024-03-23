import "./SellItems.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import React from "react";
function SellItems({currentUserID, currentUserName}) {
  // Define state variables to hold form data
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");
  const [itemType, setItemType] = useState("");
  const [file, setFile] = useState(null);
  // const [imageSrc, setImageSrc] = useState("");
  // const [submitting, setSubmitting] = useState(false);

  const goToHome = () => {
    navigate("/");
  };
 
  const onSubmitForm = async (e) => {
    e.preventDefault();
    // setSubmitting(true);
 
    const userData = {
      userId: currentUserID, // This will be the user's id
      quantity: parseInt(quantity), // Parse quantity to integer
      postingAuthor: currentUserName, // This will be the user's name
      itemName: title,
      description: description,
      itemPrice: parseFloat(price), // Parse price to integer
      itemType: itemType,
      // imageData: file,
    };

    const addPosting = async () => {
      // This function will add a post to the database
      try {
        const formdata = new FormData();
        formdata.append("file", file);
        formdata.append("userdata", JSON.stringify(userData));
        // let response = await fetch("http://127.0.0.1:5007/addPosting", {
          let response = await fetch("https://maga-inventory-catalog-184f236ac862.herokuapp.com/addPosting", {
          method: "POST",
          headers: {"Access-Control-Allow-Origin": "*"},
          body: formdata, // Convert userData to JSON string
          redirect: "follow" //20 seconds in milliseconds
        });
        if (response.ok) {
          let jsonRes = await response.json();
          console.log(jsonRes);
          alert('Listing created!');
          goToHome();
          return jsonRes['postingId']
        } else {
          console.log("Failed to add posting:", response.status);
          alert('Failed to create listing. Please ensure selling data is valid.');
        }
      } catch (error) {
        console.error("Error adding post:", error);
        alert('Failed to create listing. Please ensure selling data is valid.');
      }
    };
    addPosting();
  };

  return (
    <div id="sell-page">
      <form className="sell-form" onSubmit={onSubmitForm}>
        <h2>Create a Listing</h2>
        <div id="image-upload-container">
          <label htmlFor="file-upload" id="image-upload-label" className={file ? "image-added" : ""}>
            <img
              src="https://icons.veryicon.com/png/o/application/designe-editing/add-image-1.png"
              alt="Photo Icon"
            />
            <h3>Add Photo</h3>
          </label>
          <input
            id="file-upload"
            type="file"
            accept=".jpg, .jpeg, .png"
            onChange={(e) => setFile(e.target.files[0])}
          />
        </div>
        <input
          className="sell-input"
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <input
          className="sell-input"
          placeholder="Price"
          type="number"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          required
        />
        <input
          className="sell-input"
          placeholder="Quantity"
          type="number"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          required
        />

        <select
          className="sell-input"
          value={itemType}
          onChange={(e) => setItemType(e.target.value)}
          required
        >
          <option value="">Select Item Type</option>
          <option value="MACHINERY">MACHINERY</option>
          <option value="TOOLS">TOOLS</option>
          <option value="LIVESTOCK">LIVESTOCK</option>
          <option value="PRODUCE">PRODUCE</option>
        </select>

        <input
          className="sell-input"
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <button className="create-listing-button" type="submit">Create Listing</button>
      </form>
  </div>
  );
}

export default SellItems;
