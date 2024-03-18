# SENG401Project

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