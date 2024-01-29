# README for Backend

This README guides you through setting up and running the backend API of the application. This application is written in Python with [FastAPI](https://fastapi.tiangolo.com/) framework. It uses a `requirements.txt` file for managing dependencies and a `.env` file for configurations.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or later
- pip (Python package manager)
- A virtual environment manager (e.g., venv, virtualenv)

## Setup Instructions

1. ### Clone this repository

2. ### Create and activate the a virtual environment

   Navigate to the project directory and create a virtual environment:

   ```
   python3 -m venv venv
   ```

   Activate the virtual environment:

   ```
   source venv/bin/activate
   ```

3. ### Install dependencies

   Install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

4. ### Environment Variables

   Create a `.env` file in the root directory of the project with all the necessary database configurations. You could use `.env.example` as a reference.

5. ### Database Migration

   In order to setup the database schema, you'll need to run migrations using Alembic. Apply the migration to the database:

   ```
   alembic upgrade head
   ```

## Running the Application

To run the application, go to the project root directory and run the following command:

```
python -m uvicorn app.main:app --reload
```

## Accessing the Application

Once the server is running, you can access the application by navigating to:

```
localhost:8000
```

The automatic interactive API documentation can be accessed at:

```
localhost:8000/docs
```

## Important Note

Now you have successfully setup the backend, you can continue to setup the frontend part of the application. The frontend code can be found [here](https://github.com/jaytoy/iscc-frontend).
