import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import './Payment.css';

function Payment({currentUserID}) {

  const location = useLocation();
  const navigate = useNavigate();
  const totalPrice = location.state.totalPrice;
  const userID = 1;
 
  const generateNumbers = (start, end) => {
    const options = [];
    for (let i = start; i <= end; i++) {
      options.push(<option key={i} value={i}>{i}</option>);
    }
    return options;
  };

  const currentYear = new Date().getFullYear();

  const [selectedMonth, setSelectedMonth] = useState(1);
  const [selectedYear, setSelectedYear] = useState(currentYear);

  const [values, setValues] = useState({
    cardNumberBox: '',
    csvBox: '',
    nameBox: '',
    cityBox: '',
    billingAddressBox: '',
    billingAddress2Box: '',
    stateBox: '',
    phoneBox: '',
    zipBox: '',
    countryBox: ''
  });


  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues((prevValues) => ({
      ...prevValues,
      [name]: value
    }));
  };

  const submitPayment = async () => {
    Object.entries(values).forEach(([key, value]) => {
      console.log(`${key}: ${value}`);
    });

    if (values.cardNumberBox.length !== 16) {
      window.alert("Card number must be 16 digits");
      return;
    }
    if (values.csvBox.length !== 3) {
      window.alert("Security number must be 3 digits");
      return;
    }
    const requiredFields = ['cardNumberBox', 'csvBox', 'nameBox', 'cityBox', 'billingAddressBox', 'stateBox', 'phoneBox', 'zipBox', 'countryBox'];
    for (const field of requiredFields) {
      if (!values[field]) {
        if (field === 'cardNumberBox') {
          window.alert("Card number is required");
          return;
        }
        if (field === 'csvBox') {
          window.alert("Security number is required");
          return;
        }
        if (field === 'nameBox') {
          window.alert("Name is required");
          return;
        }
        if (field === 'cityBox') {
          window.alert("City is required");
          return;
        }
        if (field === 'billingAddressBox') {
          window.alert("Billing address is required");
          return;
        }
        if (field === 'stateBox') {
          window.alert("State is required");
          return;
        }
        if (field === 'phoneBox') {
          window.alert("Phone number is required");
          return;
        }
        if (field === 'zipBox') {
          window.alert("Zip code is required");
          return;
        }
        if (field === 'countryBox') {
          window.alert("Country is required");
          return;
        }
      }
    }
    try {
      let data = {
        userId: currentUserID
      };
      // let response = await fetch("http://127.0.0.1:5002/createOrder", {
        let response = await fetch("https://maga-controller-820d8b68274a.herokuapp.com/createOrder", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)  // Convert data to JSON string and include in the body
      });
      if (response.ok) {
        let jsonRes = await response.json();
        console.log(jsonRes, "JSON RES");
        console.log('Successfully Created Order');
        navigate('/');
      } else {
        console.log("Failed to create order", response.status);
        console.log(response, "RESPONSE");
      }
    } catch (error) {
      console.error("Error creating error", error);
    }
  };

  const [errors, setErrors] = useState({
    cardNumberError: '',
    csvError: '',
    nameError: '',
    cityError: '',
    billingAddressError: '',
    billingAddress2Error: '',
    stateError: '',
    phoneError: '',
    zipError: '',
    countryError: ''
  });


  const handleBlur = (e) => {
    const { name, value } = e.target;
    let errorMessage = '';
    // Extract field name without the "Box" suffix
    const fieldName = name.replace("Box", "");
    if (fieldName === 'cardNumber' && value.length !== 16) {
        errorMessage = 'Card number must be 16 digits';
    } 
    if (fieldName === 'csv' && value.length !== 3) {
        errorMessage = 'Security number must be 3 digits';
    }
    if (fieldName === "cardNumber" && value.length === 0) {
        errorMessage = `Card Number is required`;
    }
    if (fieldName === "csv" && value.length === 0) {
        errorMessage = `Security Number is required`;
    }
    if (fieldName === "name" && value.length === 0) {
        errorMessage = `Name is required`;
    }
    if (fieldName === "city" && value.length === 0) {
        errorMessage = `City is required`;
    }
    if (fieldName === "billingAddress" && value.length === 0) {
        errorMessage = `Billing Address is required`;
    }
    if (fieldName === "state" && value.length === 0) {
        errorMessage = `State is required`;
    }
    if (fieldName === "phone" && value.length === 0) {
        errorMessage = `Phone Number is required`;
    }
    if (fieldName === "zip" && value.length === 0) {
        errorMessage = `Zip Code is required`;
    }
    if (fieldName === "country" && value.length === 0) {
        errorMessage = `Country is required`;
    }
    
    setErrors(prevErrors => ({
      ...prevErrors,
      [`${fieldName}Error`]: errorMessage,
  }));
};


  return (
      <div className="container">
        <div className="row-text" id="billingDiv">Billing Information</div>
        <div className="row-text">
          <div className="text-box">
              <label>Card Number</label>
              <input className="billing-input" type="text" id="cardNumberBox" name="cardNumberBox" value={values.cardNumberBox} onChange={handleChange} onBlur={handleBlur} />
              {errors.cardNumberError && <div className="error-message">{errors.cardNumberError}</div>}
          </div> 
          <div className="text-box">
              <label>Security Number</label>
              <input className="billing-input" type="text" id="csvBox" name="csvBox" value={values.csvBox} onChange={handleChange} onBlur={handleBlur}/>
              {errors.csvError && <div className="error-message">{errors.csvError}</div>}
          </div>
        </div>
        <div className="row-text">
          <div className="text-box">
              <label>Name</label>
              <input className="billing-input" type="text" id="nameBox" name="nameBox" value={values.nameBox} onChange={handleChange} onBlur={handleBlur}/>
              {errors.nameError && <div className="error-message">{errors.nameError}</div>}

          </div>
          <div className="text-box">
              <label>City</label>
              <input className="billing-input" type="text" id="cityBox" name="cityBox" value={values.cityBox} onChange={handleChange} onBlur={handleBlur}/>
              {errors.cityError && <div className="error-message">{errors.cityError}</div>}
          </div>
        </div>
        <div className="row-text">
          <div className="text-box">
              <label>Billing Address</label>
              <input className="billing-input" type="text" id="billingAddressBox" name="billingAddressBox" value={values.billingAddressBox} onChange={handleChange} onBlur={handleBlur}/>
              {errors.billingAddressError && <div className="error-message">{errors.billingAddressError}</div>}
          </div>
          <div className="text-box">
              <label>State/Province</label>
              <input className="billing-input" type="text" id="stateBox"  name="stateBox" value={values.stateBox} onChange={handleChange} onBlur={handleBlur}/>
              {errors.stateError && <div className="error-message">{errors.stateError}</div>}
          </div>
        </div>
        <div className="row-text">
          <div className="text-box">
            <label>Expiration Date (Month)</label>
            <div className="month-sec">
              <select className="timeselect select-input billing-input" id="timeSelectMonth" name="timeSelectMonth" value={selectedMonth} onChange={(e) => setSelectedMonth(parseInt(e.target.value))}>
                {generateNumbers(1, 12)}
              </select>
            </div>
          </div>
          <div className="text-box">
            <label>Expiration Date (Year)</label>
            <select className="timeselect select-input billing-input" id="timeSelectYear" name="timeSelectYear" value={selectedYear} onChange={(e) => setSelectedYear(parseInt(e.target.value))}>
              {generateNumbers(currentYear, currentYear + 20)}
            </select>
          </div>
        </div>
        <div className="row-text">
          <div className="text-box">
            <label>Zip or Postal Code</label>
            <input className="billing-input" type="text" id="zipBox" name="zipBox" value={values.zipBox} onChange={handleChange} onBlur={handleBlur}/>
            {errors.zipError && <div className="error-message">{errors.zipError}</div>}
          </div>
          <div className="text-box">
            <label>Country</label>
            <input className="billing-input" type="text" id="countryBox" name="countryBox" value={values.countryBox} onChange={handleChange} onBlur={handleBlur}/>
            {errors.countryError && <div className="error-message">{errors.countryError}</div>}
          </div>
        </div>
        <div className="row-text">
          <div className="text-box">
            <label>Phone Number</label>
            <input className="billing-input" type="text" id="phoneBox" name="phoneBox" value={values.phoneBox} onChange={handleChange} onBlur={handleBlur}/>
            {errors.phoneError && <div className="error-message">{errors.phoneError}</div>}
          </div>
        </div>
        <div className="payment">
          <button className="pay-button" onClick={submitPayment} id="payButton">Pay</button>
        </div>
    </div>
  );
}

export default Payment;