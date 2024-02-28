# Todo Flask
A simple flask backend appplication to manage todo's. 


# Flask Application with MongoDB Setup Guide

This guide will walk you through setting up a Flask application with basic routes and using MongoDB as the database.

## Prerequisites
- Python (3.9) installed on your system
- `venv` module for creating virtual environments

## Installation and Setup

1. **Clone the Repository:**

    ```
   https://github.com/Yaswanth963/todo-flask.git
    ```
    
    ```
    cd todo-flask
    ```

2. **Create and Activate a Virtual Environment:**


    ```
    python3 -m venv <virtual_env_name>
    source <virtual_env_name>/bin/activate
    ```


3. **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

4. **Set Environment Variables:**
Before running the Flask application, make sure to set the necessary environment variables mentioned in `config.py`. For example:

    ```
    export MONGO_URI=mongodb://localhost:27017/todo_app
    ......
    ......
    ```

5. **Run the Flask Application:**
    
    Here you can specify the port on which you want your server to run. Also you can enable or disable debug

    ```
    flask run -p 8081 --debug
    ```



## Project Structure
```
├── app
│ ├── middleware
│ ├── models
│ ├── routes
| ├── statis
│ ├── templates
│ ├── init.py
| ├── config.py
| ├── run.py
├── requirements.txt
├── venv
|   ├── bin
|   ├── include
|   ├── lib
├── README.md
```

- `app`: Contains the main application files.
- `middleware`: Contains middleware files.
- `models.py`: Defines database models.
- `routes.py`: Defines application routes.
- `statis`: Contains all the static files (img, css, js etc..)
- `templates`: Contains HTML templates.
- `__init__.py`: Initializes the Flask application.
- `config.py`: Contains configuration variables.
- `requirements.txt`: Lists all the Python dependencies.
- `venv`: Virtual environment directory.
- `Readme.md`: Project Readme file.

## Usage
- The Flask application will run on `http://localhost:8081`.
- Visit `http://localhost:8081` in your web browser to access the application.

## Notes
- Ensure MongoDB is running on your system before starting the Flask application with proper database created.
- Update `config.py` with your specific configurations and environment variables.

This README provides a basic setup guide. Feel free to modify it according to your project requirements.
