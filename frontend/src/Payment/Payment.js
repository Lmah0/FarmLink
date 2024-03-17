import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import './Payment.css';

function Payment() {
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
    textbox1: '',
    textbox2: '',
    textbox3: '',
    textbox4: '',
    textbox5: '',
    textbox6: '',
    textbox7: '',
    textbox8: '',
    textbox9: '',
    textbox10: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues((prevValues) => ({
      ...prevValues,
      [name]: value
    }));
    console.log(values.textbox1);
  };

  const saveText = async () => {
    Object.entries(values).forEach(([key, value]) => {
      console.log(`${key}: ${value}`);
    });

    if (values.textbox1.length !== 16) {
      console.log("Card number must be 16 digits");
      return;
    }
    if (values.textbox2.length !== 3) {
      console.log("Security number must be 3 digits");
      return;
    }
    const requiredFields = ['textbox1', 'textbox2', 'textbox3', 'textbox4', 'textbox5', 'textbox6', 'textbox8', 'textbox9', 'textbox10'];
    for (const field of requiredFields) {
      if (!values[field]) {
        console.log(`${field} is required`);
        return;
      }
    }
    console.log(totalPrice)
    try {
      let response = await fetch("http://127.0.0.1:5002/createOrder", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userID),
      });
      if (response.ok) {
        let jsonRes = await response.json();
        console.log(jsonRes, "JSON RES");
        console.log('Successfully Created Order');
        navigate('/');
      } else {
        console.log("Failed to create order", response.status);
      }
    } catch (error) {
      console.error("Error creating error", error);
    }
  };


  return (
    <div>
      <div className="container">
        <div className="row">
          <div className="text-box">
            <label>Card Number</label>
            <input type="text" name="textbox1" value={values.textbox1} onChange={handleChange}/>
          </div>
          <div className="select-text">
            <div className="split-select">
              <label>Expiration Date</label>
              <div className="month-sec">
                <select className="timeselect" value={selectedMonth} onChange={(e) => setSelectedMonth(parseInt(e.target.value))}>
                  {generateNumbers(1, 12)}
                </select>
                <select className="timeselect" value={selectedYear} onChange={(e) => setSelectedYear(parseInt(e.target.value))}>
                  {generateNumbers(currentYear, currentYear + 20)}
                </select>
              </div>
            </div>
            <div className="split-text">
              <label>Security Number</label>
              <input type="text" name="textbox2" value={values.textbox2} onChange={handleChange}/>
            </div>
          </div>
        </div>
        <div className="row-text">
          <div className="row-text">Billing Information</div>
        </div>
        <div className="row">
        <div className="text-box">
            <label>Name</label>
            <input type="text" name="textbox3" value={values.textbox3} onChange={handleChange}/>
          </div>
          <div className="text-box">
            <label>City</label>
            <input type="text" name="textbox4" value={values.textbox4} onChange={handleChange}/>
          </div>
        </div>
        <div className="row">
        <div className="text-box">
            <label>Billing Address</label>
            <input type="text" name="textbox5" value={values.textbox5} onChange={handleChange}/>
          </div>
          <div className="text-box">
            <label>State/Province</label>
            <input type="text" name="textbox6" value={values.textbox6} onChange={handleChange}/>
          </div>
        </div>
        <div className="row">
        <div className="text-box">
            <label>Billing Address, line 2</label>
            <input type="text" name="textbox7" value={values.textbox7} onChange={handleChange}/>
          </div>
          <div className="text-box">
            <label>Zip or Postal Code</label>
            <input type="text" name="textbox8" value={values.textbox8} onChange={handleChange}/>
          </div>
        </div>
        <div className="row">
        <div className="text-box">
            <label>Country</label>
            <input type="text" name="textbox9" value={values.textbox9} onChange={handleChange}/>
          </div>
          <div className="text-box">
            <label>Phone Number</label>
            <input type="text" name="textbox10" value={values.textbox10} onChange={handleChange}/>
          </div>
        </div>
        <div className="payment">
          <button className="pay-button" onClick={saveText}>Pay</button>
        </div>
      </div>
    </div>
  );
}

export default Payment;