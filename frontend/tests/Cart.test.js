import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import Cart from '../src/Cart/Cart';

// Mock the useNavigate hook
jest.mock('react-router-dom', () => ({
  useNavigate: jest.fn(),
}));

// Mocking console.error to prevent it from outputting during the test
console.error = jest.fn();


describe('renderCart', () => {
  test('renders without crashing', () => {
    render(<Cart />);
  });

  test('displayCart', () => {
    const { getByText } = render(<Cart />);
    expect(getByText('Items in Cart')).toBeInTheDocument();
  });

  test('displayTotalPrice', () => {
    const { getByText } = render(<Cart />);
    expect(getByText('Total Price: $0')).toBeInTheDocument();
  });

  test('displayCheckoutButton', () => {
    const { getByText } = render(<Cart />);
    expect(getByText('Checkout Now')).toBeInTheDocument();
  });
});
