import React from 'react';
import { render } from '@testing-library/react';
import HomePageEmpty from '../src/HomePage/HomePageEmpty';

// Mocking react-router-dom module
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
}));


describe('HomePageEmpty component', () => {
  test('renders "No Postings Currently Available" message', () => {
    const { getByText } = render(<HomePageEmpty />);
  });
});
