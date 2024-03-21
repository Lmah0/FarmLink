# SENG401Project

### Backend Deployment URLs
| service | URL |
|---------|-----|
| controller | https://maga-controller-820d8b68274a.herokuapp.com |
| user management | https://maga-user-management-7c1e7511f413.herokuapp.com |
| checkout | https://maga-checkout-6a70c9b6586c.herokuapp.com |
| inventory catalog | https://maga-inventory-catalog-184f236ac862.herokuapp.com |
| shopping cart | https://maga-shopping-cart-99f9049cebbc.herokuapp.com |

# How to start Frontend
npm install react-scripts --save
npm install react-router-dom
then npm start
must be in the frontend directory

# Ports
# Must be in the backend/microservices directory
flask --app user_management_service run --debug --port 5000
flask --app shopping_cart_service run --debug --port 5008
flask --app inventory_catalog_service run --debug --port 5007
flask --app checkout_service run --debug --port 5009

# Must be in the backend/controllers directory
flask --app controller run --debug --port 5002
