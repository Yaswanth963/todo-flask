# Todo Flask
A simple flask backend appplication to manage todo's. 


# Flask Application with MongoDB Setup Guide

This guide will walk you through setting up a Flask application with basic routes and using MongoDB as the database.

## Prerequisites
- Python (3.9) installed on your system
- `venv` module for creating virtual environments

## Installation and Setup

1. **Clone the Repository:**

   [repository_url](https://github.com/Yaswanth963/todo-flask.git)
    
    cd <repository_directory>

2. **Create and Activate a Virtual Environment:**



python3 -m venv <virtual_env_name>
source <virtual_env_name>/bin/activate



3. **Install Dependencies:**

pip install -r requirements.txt


4. **Set Environment Variables:**
Before running the Flask application, make sure to set the necessary environment variables mentioned in `config.py`. For example:

export MONGO_URI=mongodb://localhost:27017/todo_app


5. **Run the Flask Application:**

flask run -p 8081 --debug



## Project Structure

├── README.md
├── app
│ ├── init.py
│ ├── config.py
│ ├── models.py
│ ├── routes.py
│ └── templates
│ └── index.html
├── requirements.txt
└── venv
├── bin
├── include
├── lib
└── share



- `app`: Contains the main application files.
- `__init__.py`: Initializes the Flask application.
- `config.py`: Contains configuration variables.
- `models.py`: Defines database models.
- `routes.py`: Defines application routes.
- `templates`: Contains HTML templates.

- `requirements.txt`: Lists all the Python dependencies.

- `venv`: Virtual environment directory.

## Usage
- The Flask application will run on `http://localhost:8081`.
- Visit `http://localhost:8081` in your web browser to access the application.

## Notes
- Ensure MongoDB is running on your system before starting the Flask application.
- Update `config.py` with your specific configurations and environment variables.

This README provides a basic setup guide. Feel free to modify it according to your project requirements