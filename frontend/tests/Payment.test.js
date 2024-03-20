import React from 'react';
import { render } from '@testing-library/react';
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

describe('Payment Component', () => {
  test('Renders Payment component without crashing', () => {
    render(<Payment />);
  });

  test('Displays Pay button', () => {
    const { getByText } = render(<Payment />);
    expect(getByText('Pay')).toBeInTheDocument();
  });
});
