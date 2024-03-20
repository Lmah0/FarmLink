import LoginPage from '../src/UserPages/LoginPage';
import React from 'react';
import { render, fireEvent, waitFor, getByLabelText} from '@testing-library/react/pure';

// Mocking the useNavigate hook
jest.mock('react-router-dom', () => ({
  useNavigate: jest.fn(),
}));

// test that the login form is rendered
describe('LoginPage Component', () => {
  it('renders without crashing', () => {
    render(<LoginPage />);
  });


});
