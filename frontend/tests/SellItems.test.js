import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import SellItems from '../src/SellItems/SellItems';

describe('SellItems Component', () => {
  it('renders the form elements', () => {
    const { getByPlaceholderText, getByText } = render(<SellItems />);

    expect(getByPlaceholderText('Title')).toBeInTheDocument();
    expect(getByPlaceholderText('Price')).toBeInTheDocument();
    expect(getByPlaceholderText('Quantity')).toBeInTheDocument();
    expect(getByPlaceholderText('Item Type')).toBeInTheDocument();
    expect(getByPlaceholderText('Description')).toBeInTheDocument();
    expect(getByText('Create Listing')).toBeInTheDocument();
  });

  it('submits the form with correct data', async () => {
    const mockFetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ success: true }),
      })
    );
    global.fetch = mockFetch;

    const { getByPlaceholderText, getByText } = render(<SellItems />);

    fireEvent.change(getByPlaceholderText('Title'), { target: { value: 'Test Title' } });
    fireEvent.change(getByPlaceholderText('Price'), { target: { value: '10' } });
    fireEvent.change(getByPlaceholderText('Quantity'), { target: { value: '5' } });
    fireEvent.change(getByPlaceholderText('Item Type'), { target: { value: 'Test Type' } });
    fireEvent.change(getByPlaceholderText('Description'), { target: { value: 'Test Description' } });

    fireEvent.click(getByText('Create Listing'));

    await waitFor(() => expect(mockFetch).toHaveBeenCalled());

    // You can add more assertions here based on the response behavior
  });

  it('displays an error message if submission fails', async () => {
    const mockFetch = jest.fn(() =>
      Promise.resolve({
        ok: false,
        statusText: 'Internal Server Error',
      })
    );
    global.fetch = mockFetch;
  
    const { getByPlaceholderText, getByText, findByText } = render(<SellItems />);
  
    fireEvent.change(getByPlaceholderText('Title'), { target: { value: 'Test Title' } });
    fireEvent.change(getByPlaceholderText('Price'), { target: { value: '10' } });
    fireEvent.change(getByPlaceholderText('Quantity'), { target: { value: '5' } });
    fireEvent.change(getByPlaceholderText('Item Type'), { target: { value: 'Test Type' } });
    fireEvent.change(getByPlaceholderText('Description'), { target: { value: 'Test Description' } });
  
    fireEvent.click(getByText('Create Listing'));
  
    await waitFor(() => expect(mockFetch).toHaveBeenCalled());
  
    // Use findByText to wait for the error message to appear
    const errorMessage = await findByText(/Error: Internal Server Error/i);
    expect(errorMessage).toBeInTheDocument();
  });
});
