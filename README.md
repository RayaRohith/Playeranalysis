Backend application framework, README ready to be implemented.

## I. Package needed for running the project

### 1. Python 3.12, can be download from [https://www.python.org/downloads/]

### 2. bson package, use pip install command in the terminal or from IDE like Pycharm

### 3. flask package, use pip install command in the terminal or from IDE like Pycharm
Flask is the backend framework used in this project

### 4. pymongo package, use pip install command in the terminal or from IDE like Pycharm
Used to facilitate the MongoDB connection used in this project

### 5. werkzeug.security, use pip install command in the terminal or from IDE like Pycharm
Used to hash the passcode of users accounts for security

### 6. MongoDB, although the project employs NoSQL, a MongoDB engine still needs to be implemented on the server before the project is ran.

## II. Project Sturcture

All front end codes are stored in \templetes folder in the main branch, it contains all html codes necessary for the complete logic of the websites.

All back end codes are stored in app.py, we uses flask as the backend develepment framework.

Documentations are stored in Project's gitlab wiki, it contains information of Risk assessment, CI/CD pipeline and Databases structure.

the data folder 3 json files that needs to be imported into mongoDB beforehand, so there are example data on the website.

Due to the purpose of demonstration, currently the project can only be run locally, which means the project needs to be on the same physical mechine as the MongoDB engine, since the database connection is set up locally.




