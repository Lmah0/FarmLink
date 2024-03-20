import SignUpPage from '../src/UserPages/SignUpPage';
import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';

// Mocking the useNavigate hook
jest.mock('react-router-dom', () => ({
  useNavigate: () => jest.fn(),
}));

describe('<SignUpPage />', () => {
  test('renders sign up form', () => {
    const { getByLabelText } = render(<SignUpPage />);
    
    expect(getByLabelText('Phone Number')).toBeInTheDocument();
    expect(getByLabelText('Email')).toBeInTheDocument();
    expect(getByLabelText('Password')).toBeInTheDocument();
    expect(getByLabelText('Role')).toBeInTheDocument();
    expect(getByLabelText('Profile Bio')).toBeInTheDocument();
  });


  
});

