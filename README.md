# SENG401Project

# Deployed Application URL: https://magaseng401.netlify.app/ 

# How to start Frontend
npm install react-scripts --save
npm install react-router-dom
npm install react-typed
then run 'npm start' in the frotend directory

# Running the main branch:
Currently all endpoints in the main branch are configured to make use of the globally deployed endpoints on Heroku. By starting the frontend on main, everything will be functional. Note that developer branches may still be configured to run locally as separate Flask servers.

Any pushed to the main branch will automatically update the Netlify frontend deployment. Ensure any pushes to main are approved via Pull Request.

# Running locally:
## Must be in the backend/microservices directory
flask --app user_management_service run --debug --port 5000
flask --app shopping_cart_service run --debug --port 5008
flask --app inventory_catalog_service run --debug --port 5007
flask --app checkout_service run --debug --port 5009

## Must be in the backend/controllers directory
flask --app controller run --debug --port 5002
