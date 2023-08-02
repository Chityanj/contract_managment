# Contract Managment 
## Description
This project is a Django web application that allows users to manage client contracts and employee details for a company providing maintenance services.
![image](https://github.com/Chityanj/contract_managment/assets/20499500/36c328fc-7fbd-480e-bf69-355eb4339c19)
![image](https://github.com/Chityanj/contract_managment/assets/20499500/203768ed-315e-442b-a65f-df3d4d6bdf7c)


## Features
- Add and manage clients and employees.
- Map employees to clients for service assignments.
- Add multiple service dates for each client.
- Public display of client and employee information (no contract dates shown).
- Private section with more functionality and confidential information.

## Setup and Installation
- Clone the repository to your local machine.
- Install the required dependencies using pip install -r requirements.txt.
- Set up your database by running python manage.py migrate.
- Start the development server with python manage.py runserver.

## Usage
- Navigate to the admin interface (http://localhost:8000/admin/) and log in with your superuser credentials to add clients and employees.
- Use the provided forms to add service dates and employee mappings to clients.
- Access the public display section (http://localhost:8000/public/) to view client and employee information without contract dates.
- Access the private section (http://localhost:8000/private/) for more functionality and access to contract generation and acceptance.
## Project Structure
```contract_management_app/: Django app directory containing models, views, and forms for managing contracts, clients, and employees.
media/: Directory to store uploaded contract templates and generated PDF contracts.
static/: Directory to store static files (CSS, JS) for the project.
templates/: Directory to store HTML templates for the views.
```
## Technologies Used
- Django: Web framework for building the application.
- Bootstrap: Frontend library for responsive design.
- python-docx: Library for modifying contract templates and generating PDF contracts.
# Notes
This project is intended for educational purposes and may require additional security measures for production use.
Confidential contract details are only accessible in the private section and restricted to authorized users.
Feel free to add any other relevant details or instructions specific to your project. Once you have completed the public section of the project, let me know, and we can move on to implementing the private section with more functionality.
