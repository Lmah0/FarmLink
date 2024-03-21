import SignUpPage from '../src/UserPages/SignUpPage';
import React from 'react';
import { render, fireEvent } from '@testing-library/react';

// Mocking the useNavigate hook
jest.mock('react-router-dom', () => ({
  useNavigate: jest.fn(),
}));
// Mocking console.error to prevent it from outputting during the test
console.error = jest.fn();

describe('<SignUpPage />', () => {
  it('renderSignUp', () => {
    render(<SignUpPage />)
  });

  it('submitSignUpFormButton', () => {
    const { getByRole } = render(<SignUpPage />);
    fireEvent.submit(getByRole('button', { name: /sign up/i }));
  });
});
