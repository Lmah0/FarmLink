import React from 'react';
import { render } from '@testing-library/react';
import HomePageEmpty from '../src/HomePage/HomePageEmpty';

// Mocking react-router-dom module
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
}));

describe('renderHomePageSignUp', () => {
  test('renders "Sign Up" button', () => {
    const { getByText } = render(<HomePageEmpty />);
    const signUpButton = getByText('Sign Up');
    expect(signUpButton).toBeInTheDocument();
  });

  test('renderLoginButton', () => {
    const { getByText } = render(<HomePageEmpty />);
    const loginButton = getByText('Login');
    expect(loginButton).toBeInTheDocument();
  });
});
