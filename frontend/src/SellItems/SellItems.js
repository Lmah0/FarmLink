import "./SellItems.css";
import { useState } from "react";

function SellItems() {
  // Define state variables to hold form data
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");
  const [itemType, setItemType] = useState("");
  const [file, setFile] = useState(null);
  const [imageSrc, setImageSrc] = useState("");

  const [submitting, setSubmitting] = useState(false);

  const onSubmitForm = async (e) => {
    e.preventDefault();
    setSubmitting(true);

    const userData = {
      userId: 1, // This will be the user's id
      quantity: parseInt(quantity), // Parse quantity to integer
      postingAuthor: "Eric Mei", // This will be the user's name
      itemName: title,
      description: description,
      itemPrice: parseFloat(price), // Parse price to integer
      itemType: itemType,
      // imageData: file,
    };

    // console.log(userData, "USER DATA");
    await fetch("http://127.0.0.0.1:5007/addPosting", {
      method: "POST",
      body: JSON.stringify(userData), // Convert userData to JSON string
      headers: {
        "Content-Type": "application/json",
      },
      timeout: 20000, //20 seconds in milliseconds
    })
      .then((response) => {
        if (response.ok) {
          let res = response.json();
          console.log(res, "RESPONSE");
          return res;
        } else {
          throw new Error("Network response was not ok");
        }
      })
      .then((data) => {
        console.log(data, "data");
        setSubmitting(false);
      })
      .catch((error) => {
        setSubmitting(false);
      });
  };

  // Function to handle file upload
  const handleFileChange = (e) => {
    const reader = new FileReader();
    const file = e.target.files[0];

    reader.onloadend = () => {
      setImageSrc(reader.result);
    };

    if (file) {
      reader.readAsDataURL(file);
    }
  };

  return (
    <>
      <div id="sell-items-main-div">
        <h2>Create a Listing</h2>
        <form onSubmit={onSubmitForm}>
          <div id="image-upload-container">
            <label htmlFor="file-upload" id="image-upload-label">
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
              // onChange={handleFileChange}
              // required
            />
          </div>
          {/* <h2>Required</h2> */}
          {/* <h3>Be as Descriptive as Possbile</h3>  */}
          <input
            type="text"
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
          <input
            placeholder="Price"
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            required
          />
          <input
            placeholder="Quantity"
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            required
          />

          <select
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
            type="text"
            placeholder="Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
          <button type="submit">Create Listing</button>
        </form>
      </div>
    </>
  );
}

export default SellItems;
