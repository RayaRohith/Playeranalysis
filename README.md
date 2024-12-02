# Player Health Recommendation System
The Player Health Recommendation System helps track and manage football players' health by offering personalized treatment suggestions, including medication, physiotherapy, and training plans. Built with Flask, Django, MongoDB, and Jenkins, it ensures smooth backend operations and continuous updates.

# Overiew of the project

The Player Health Recommendation System is a web-based platform designed to help football teams monitor and manage the health of their players. When a player is injured or experiencing medical issues, they can input their symptoms into the system. Based on this input, the platform provides tailored recommendations for medication, physiotherapy, and training plans to help players recover and return to their peak performance. The system is designed for use by players, coaches, and medical staff, ensuring that the health of each player is effectively managed.

This system is built using modern technologies like Flask, Django, MongoDB, and Jenkins. These technologies ensure smooth backend operations, scalability, and continuous updates. The Flask framework handles the web application's backend, while Django provides a robust structure for more complex functionalities. MongoDB is used for managing player health data, and Jenkins automates the CI/CD pipeline, allowing for continuous integration and deployment of the system.

# Tools and Technologies
Python 3.12: The programming language used for building the system's backend. Download it from Python.org.
Flask: A lightweight web framework used to handle the backend and user requests.
Django: Handles complex functionalities and provides additional features for user management and data handling.
MongoDB: A NoSQL database that stores player health data, treatment history, and recommendations.
Werkzeug: Used for secure password hashing and user authentication.
Jenkins: Automates the deployment process, ensuring smooth updates and integration.
GitLab: The repository for code management, version control, and collaboration.

# Installation and Setup
To set up the Player Health Recommendation System locally, follow these steps:

Install Python 3.12 from Python.org.
Install the necessary packages using pip install flask, pip install django, pip install pymongo, and pip install werkzeug for the respective libraries.
Set up MongoDB locally to store the data. Ensure MongoDB is running on the same machine as the project.
Import the sample data from the data folder into MongoDB to populate the system with initial player health records.

# Structure of the Project

Frontend: All HTML files (such as login pages, player health forms, and recommendation displays) are stored in the templates folder. These are responsible for the user interface.
Backend: The logic for processing user inputs, generating recommendations, and interacting with the database is in app.py. This file is the core of the backend system and uses Flask for web routing.
Database: MongoDB stores player health data, including injuries, treatments, and recommendations. The data folder contains JSON files that should be imported into MongoDB.
Documentation: All project-related documentation, including the CI/CD pipeline, risk assessment, and database structure, is available in the project's GitLab wiki.
Implementation and CI/CD Pipeline
The project follows a structured development and deployment process:

# Source Code Repository:

The code is managed in GitLab, which serves as the central repository. Developers commit their code regularly to GitLab to keep track of changes and collaborate effectively.
# Continuous Integration (CI):

The system undergoes testing in a VirtualBox environment to simulate real-world conditions. The goal is to ensure that the system works as expected before deployment.
Mock accounts for players, managers, and medical staff are created to test different roles and permissions in the system.
# Continuous Deployment (CD):

Jenkins automates the deployment process, ensuring that the latest code changes are automatically tested and deployed to the live environment.
Feedback about any system bugs or issues discovered during testing is communicated via WhatsApp, allowing for quick resolution of problems.
Regular discussions and improvement sessions are held to ensure the system is continuously updated and enhanced based on feedback.
Usability Testing and Results
During usability testing, the Player Health Recommendation System was shared with a group of users who interacted with the system. They were asked to explore the website, providing feedback based on their experience. No major issues or bugs were reported, suggesting that the system is stable and intuitive to use.


Log-in page
![image](https://github.com/user-attachments/assets/8b4dcda7-cb8f-4562-a057-e5103a748c1d)


Page used in Usability testing:
![image](https://github.com/user-attachments/assets/7e09e23f-2b94-4483-80d7-f462be92c8ea)




