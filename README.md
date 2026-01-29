# Full-Stack Developer Technical Challenge

## Author

Ana Sequeira

---

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose (included with Docker Desktop)

---

### Running the Application

1. Clone the repository:
git clone <repository-url>
cd task_manager

2. Build and start the containers:
docker compose up --build

This will start:
- Django application
- PostgreSQL database
- Nginx reverse proxy

3. Run database migrations:
docker compose exec web python manage.py migrate

4. Create a superuser:
docker compose exec web python manage.py createsuperuser

5. Access the application:

- Application: http://localhost  
- Admin panel: http://localhost/admin  
- Login using the superuser, either directly in the customer facing app(http://localhost) or 
- to the backoffice(http://localhost/admin) to create a test user

---

## Approach

The goal of this project was to build a clean, production-style CRUD application.

- **Django** was used for the backend to leverage its built-in authentication and ORM.
- **PostgreSQL** was chosen to reflect a real-world production database.
- **Tailwind CSS** was used to create a clean, responsive user interface with minimal overhead.
- **Docker and Docker Compose** were used to ensure consistent local setup and easy onboarding.
- **Nginx** was added as a reverse proxy to simulate a production deployment architecture.

The project was developed incrementally, in the same order as mentioned above, by building each part of the solution step by step and tests between phases.
Focus was on clarity and maintainability without unnecessary complexity.

After the initial assignment, I've improved the solution by adding a REST API.
The API is documented using Swagger and can be access at: http://localhost/api/docs

---