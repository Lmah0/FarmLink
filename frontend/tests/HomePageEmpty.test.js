import React from 'react';
import { render } from '@testing-library/react';
import HomePageEmpty from '../src/HomePage/HomePageEmpty';

describe('HomePageEmpty component', () => {
  test('renders "No Postings Currently Available" message', () => {
    const { getByText } = render(<HomePageEmpty />);
    const emptyHolderElement = getByText('No Postings Currently Available');
    expect(emptyHolderElement).toBeInTheDocument();
  });
});
