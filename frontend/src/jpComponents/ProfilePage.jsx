// src/components/PaymentPage.jsx
import React, { useState } from 'react';

const PaymentPage = () => {
    const [creditCardNumber, setCreditCardNumber] = useState('');
  const [CVV, setCVV] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');

  const handlePayment = (e) => {
    e.preventDefault();

    if (firstName && lastName && creditCardNumber && CVV) {
      alert('Payment successful!');
    } else {
      alert('Please fill in all fields.');
    }
  };

  return (
    <div>
      <h2>Sample Payment Page</h2>
      <h3> Order Summary</h3>
      <p>Items(# of items)</p>
      <p>GST:</p>
      <p>Total:</p>

      <h3> Payment Info:</h3>
      <form onSubmit={handlePayment}>
        <label>
          First Name:
          <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
        </label>
        <br />
        <label>
          Last Name:
          <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} />
        </label>
        <br />
        <label>
          Credit Card:
          <input type="text" value={creditCardNumber} onChange={(e) => setCreditCardNumber(e.target.value)} />
        </label>
        <br />
        <label>
          CVV:
          <input type="text" value={CVV} onChange={(e) => setCVV(e.target.value)} />
        </label>
        <br />
        <button type="submit">Place Order</button>
      </form>
    </div>
    );
};

export default PaymentPage;
