import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Payment from '../src/Payment/Payment';

// Mocking react-router-dom module
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
  useLocation: jest.fn().mockReturnValue({
    state: {
      totalPrice: 100, // Mocking the state data needed by the Payment component
    },
  }),
}));

// Mocking console.error to prevent it from outputting during the test
console.error = jest.fn();

describe('renderPayment', () => {
  test('Renders Payment component without crashing', () => {
    render(<Payment />);
  });

  test('displayPayButton', () => {
    const { getByText } = render(<Payment />);
    expect(getByText('Pay')).toBeInTheDocument();
  });

  test('alertShownWhenFieldMissed', () => {
    // Spy on window.alert
    const alertSpy = jest.spyOn(window, 'alert').mockImplementation(() => {});

    const { getByText } = render(<Payment />);

    // Click Pay button without filling any required fields
    fireEvent.click(getByText('Pay'));

    // Assert that window.alert was called with the expected message
    expect(alertSpy).toHaveBeenCalledWith('Card number must be 16 digits');

    // Restore the original implementation of window.alert
    alertSpy.mockRestore();
  });
});
