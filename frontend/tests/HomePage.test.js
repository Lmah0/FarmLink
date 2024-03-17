import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import HomePage from '../src/HomePage/HomePage';

describe('HomePage component', () => {
    const items = [
      {
        id: 1,
        posting_author: 'John Doe',
        posting_item: { name: 'Product A', price: 10 },
        quantity: 5,
        description: 'Description for Product A',
      },
      {
        id: 2,
        posting_author: 'Jane Smith',
        posting_item: { name: 'Product B', price: 20 },
        quantity: 10,
        description: 'Description for Product B',
      },
    ];
  
    test('renders all items correctly', () => {
      const { getByText } = render(<HomePage items={items} />);
      
      items.forEach(item => {
        expect(getByText(item.posting_item.name)).toBeInTheDocument();
        expect(getByText(`Price: $${item.posting_item.price}`)).toBeInTheDocument();
      });
    });
  
    test('toggles item details on click', () => {
      const { getByText } = render(<HomePage items={items} />);
      
      const firstItem = getByText(items[0].posting_item.name);
      fireEvent.click(firstItem);
  
      expect(getByText(`Seller: ${items[0].posting_author}`)).toBeInTheDocument();
      expect(getByText(`Quanity Avaliable: ${items[0].quantity}`)).toBeInTheDocument();
      expect(getByText(`Description: ${items[0].description}`)).toBeInTheDocument();
  
      fireEvent.click(firstItem); // Click again to toggle back
      expect(queryByText(`Seller: ${items[0].posting_author}`)).not.toBeInTheDocument();
      expect(queryByText(`Quanity Avaliable: ${items[0].quantity}`)).not.toBeInTheDocument();
      expect(queryByText(`Description: ${items[0].description}`)).not.toBeInTheDocument();
    });
  });