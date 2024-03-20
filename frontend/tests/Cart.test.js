import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import Cart from '../src/Cart/Cart';

// Mock the useNavigate hook
jest.mock('react-router-dom', () => ({
  useNavigate: jest.fn(),
}));

describe('Cart Component', () => {
  test('renders without crashing', () => {
    render(<Cart />);
  });

  test('displays cart items', () => {
    const { getByText } = render(<Cart />);
    expect(getByText('Items in Cart')).toBeInTheDocument();
  });

  test('displays total price', () => {
    const { getByText } = render(<Cart />);
    expect(getByText('Total Price: $0')).toBeInTheDocument();
  });

  test('displays checkout button', () => {
    const { getByText } = render(<Cart />);
    expect(getByText('Checkout Now')).toBeInTheDocument();
  });
});
