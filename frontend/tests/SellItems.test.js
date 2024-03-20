
import SellItems from '../src/SellItems/SellItems';

import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { useNavigate } from 'react-router-dom';

// Mocking react-router-dom module
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
}));

describe('SellItems Component', () => {
  it('renders without crashing', () => {
    render(<SellItems />);
  });

  it('submits form with correct data', () => {
    const navigateMock = jest.fn();
    useNavigate.mockReturnValue(navigateMock);

    const { getByPlaceholderText, getByText } = render(<SellItems />);

    const titleInput = getByPlaceholderText('Title');
    const priceInput = getByPlaceholderText('Price');
    const quantityInput = getByPlaceholderText('Quantity');
    const descriptionInput = getByPlaceholderText('Description');
    const createListingButton = getByText('Create Listing');

    fireEvent.change(titleInput, { target: { value: 'Test Title' } });
    fireEvent.change(priceInput, { target: { value: '10' } });
    fireEvent.change(quantityInput, { target: { value: '5' } });
    fireEvent.change(descriptionInput, { target: { value: 'Test Description' } });

    fireEvent.click(createListingButton);

    expect(navigateMock).toHaveBeenCalledWith('/');
  });
});
