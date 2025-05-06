# Description
A simple Django-based API application

### 1. Set up environment variables
Copy the example `.env` file:

cp .env_example .env

### 3. Build the Docker containers
docker-compose build --no-cache

### 4. Start the application
docker-compose up
The app will be available at: [http://0.0.0.0:8000](http://0.0.0.0:8000)


## Code Formatting
To automatically format code:
make fix

## API Documentation
Once the app is running, access the Swagger UI at:
http://0.0.0.0:8000/docs
