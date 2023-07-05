# Dockerized Flask Mongo App Project

This project demonstrates how to containerize a Flask web application with a MongoDB database using Docker. It provides a basic setup for running a Flask app with MongoDB in a Docker environment.

## Features

- Dockerized Flask web application
- Integration with MongoDB database
- Docker Compose for easy container orchestration
- Basic user authentication and CRUD operations
- API endpoints for interacting with the database

## Prerequisites

Make sure you have the following prerequisites installed on your machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:


git clone https://github.com/h93n/Dockerized-flask-Mongo-App-Project.git


2. Change to the project directory:


cd Dockerized-flask-Mongo-App-Project


3. Build and start the Docker containers:


docker-compose up -d


4. Open your web browser and access the application at `http://localhost:5000`.

5. You can register a new user and log in to access the protected routes.

## Project Structure

The project has the following structure:

- `app`: Contains the Flask web application code
- `app/static`: Static files (CSS, JS, images)
- `app/templates`: HTML templates
- `db`: MongoDB data directory
- `docker`: Docker-related files
- `docker-compose.yml`: Docker Compose configuration file

## Configuration

The Flask application and MongoDB connection settings can be configured in the `.env` file. Make sure to update the values as needed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).



Please note that the generated README file is a starting point and you may need to customize it further based on your specific requirements and project details.
