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

  test('displays added objects correctly', async () => {
    const { getByText } = render(<Cart />);
    fireEvent.click(getByText('Here is where the Entries will be')); // Click to add an object
    await waitFor(() => {
      expect(getByText('Object 1')).toBeInTheDocument(); // Check if added object is displayed
    });
  });

  test('calculates total price correctly', async () => {
    const { getByText } = render(<Cart />);
    fireEvent.click(getByText('Here is where the Entries will be')); // Add an object
    fireEvent.click(getByText('Here is where the Entries will be')); // Add another object
    await waitFor(() => {
      expect(getByText('Total Price: $79.98')).toBeInTheDocument(); // Check if total price is calculated correctly
    });
  });

  test('navigates to payment page when pay button is clicked', async () => {
    const { getByText } = render(<Cart />);
    fireEvent.click(getByText('Here is where the Entries will be')); // Add an object
    fireEvent.click(getByText('Pay Price')); // Click on pay button
    await waitFor(() => {
      expect(window.location.href).toContain('/Payment'); // Check if navigation occurred
    });
  });
});
