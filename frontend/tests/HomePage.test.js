import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import HomePage from '../src/HomePage/HomePage';

// Mocking react-router-dom module
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
}));

describe('HomePage component', () => {
  const mockItems = [
    {
      id: 1,
      image: 'mockImage1',
      posting_author: 'mockSeller1',
      posting_item: { name: 'mockItem1', price: 10 },
      quantity: 5,
      description: 'mockDescription1',
    },
    {
      id: 2,
      image: 'mockImage2',
      posting_author: 'mockSeller2',
      posting_item: { name: 'mockItem2', price: 20 },
      quantity: 10,
      description: 'mockDescription2',
    },
  ];

  const mockLoading = false;
  const mockCurrentUserID = 'mockUserID';
  const mockCurrentRole = 'FARMER';

  test('renderLoadingMessage', () => {
    const { getByText } = render(
      <HomePage
        items={[]}
        loading={true}
        currentUserID={mockCurrentUserID}
        currentRole={mockCurrentRole}
      />
    );
    const loadingMessage = getByText('Loading...');
    expect(loadingMessage).toBeInTheDocument();
  });

  test('rendersMainContainer', () => {
    const { getByTestId } = render(
      <HomePage
        items={mockItems}
        loading={mockLoading}
        currentUserID={mockCurrentUserID}
        currentRole={mockCurrentRole}
      />
    );

  });

  test('sellButtonRenderedForSellers', () => {
    const { getByText } = render(
      <HomePage
        items={mockItems}
        loading={mockLoading}
        currentUserID={mockCurrentUserID}
        currentRole={mockCurrentRole}
      />
    );
    const sellButton = getByText('Sell');
    expect(sellButton).toBeInTheDocument();
  });

  test('noSellButtonRenderedForBuyer', () => {
    const { queryByText } = render(
      <HomePage
        items={mockItems}
        loading={mockLoading}
        currentUserID={mockCurrentUserID}
        currentRole="CUSTOMER"
      />
    );
    const sellButton = queryByText('Sell');
  });

  test('expands item box when clicked', () => {
    const { getByAltText, getByText } = render(
      <HomePage
        items={mockItems}
        loading={mockLoading}
        currentUserID={mockCurrentUserID}
        currentRole={mockCurrentRole}
      />
    );

  });


});
