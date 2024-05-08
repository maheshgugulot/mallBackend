## Mall Backend 

## Description
This project is an application designed to manage employee authentication, product management, customer management, and billing for a business. It provides the essential functionalities required for a business to operate smoothly, including authentication of employees, CRUD operations for products and customers, and billing functionality using the cash payment method.

## Mandatory Features
- Authenticate employees
- Add, update, and delete products to/from the system
- Add, update, and delete customers
- Bill customers (Only cash payment method - No need for any integrations)

## Deployment
The application is deployed on [Render](https://render.com/).

## Deployment Details
- Cloud Platform: [Render]
- Database: Postgres
- API Documentation: Swagger (via drf-spectacular)

## Installation
To install and run this application locally, follow these steps:
1. Clone the repository: `git clone [GitHub URL]`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the database and configure the database connection settings in `settings.py`
4. Run the migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## API Endpoints
- **Authentication**: 
    - `/api/auth/login/` (POST): Endpoint for employee login
- **Products**:
    - `/api/products/` (GET, POST): Endpoint for listing and adding products
    - `/api/products/<id>/` (GET, PUT, DELETE): Endpoint for retrieving, updating, and deleting a specific product
- **Customers**:
    - `/api/customers/` (GET, POST): Endpoint for listing and adding customers
    - `/api/customers/<id>/` (GET, PUT, DELETE): Endpoint for retrieving, updating, and deleting a specific customer
- **Billing**:
    - `/api/bill/` (POST): Endpoint for billing a customer
    
## Technologies Used
- Django: Python web framework for building the backend
- PostgreSQL: Relational database management system
- drf-spectacular: Django package for generating OpenAPI documentation

## Contributors
- [Mahesh](https://github.com/maheshgugulot/mallBackend)

