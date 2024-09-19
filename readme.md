## Getting Started with FastAPI

-  This repo is meant to provide some starter files for FastAPI and includes instructions on how to get started. Simply fork this repo and you're good to get started on your own project!
-  This repo is based on the official [FastAPI Docs SQL Database Tutorial](https://fastapi.tiangolo.com/tutorial/sql-databases/). Find more information there.

### Create a virtual environment and activate it

-  To create a virtual environment named `myenv` use command `python -m venv myenv`
-  To activate the virtual environment, use `myenv\Scripts\activate` (Windows cmd), `source myenv/Scripts/activate` (Windows bash), or alternatively `source myenv/bin/activate` (if `python -m venv myenv` created a `myenv/bin` folder instead of `myenv/Scripts` folder; this usually occurs in Mac or Linux).

### Install FastAPI

-  This repo does not include downloaded dependencies, so you will need to install them.
-  Use `pip install "fastapi[standard]"` to install fastAPI with optional dependencies or `pip install fastapi` without optional dependencies.

### Run the Server

-  To run the server use command `fastapi dev main.py`

## Adaptations

-  The FastAPI tutorial was adapted to have a weather app that gets the weather from openweathermap. This requires signing up for an API key.
-  Secrets were stored in a .env file. For convenience, a file `.env copy` is included in this repo. Rename the file to .env and change the keys to your own secrets.

## Running the project

-  Once all dependencies are installed, you can run the project with the command `uvicorn weather_app.main:app --reload`.
-  Navigate to `127.0.0.1:8000/docs` for the Swagger interactive documentation, where you can view and interact with each endpoint.
