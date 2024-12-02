# Player Health Recommendation System




# Installation and Tools
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

# Implementation
1. Working prototype All the files are uploaded to the gitlab repository and below is the codebase for it
2. code base ( screen shot of the repo)

   ![Screenshot 2024-04-04 154921.png](uploads/a014c87bca6a1bce549545e0528bd988/Screenshot_2024-04-04_154921.png)
3. Deployment of CI/CD pipeline

To construct a sophisticated and academically inclined Continuous Deployment (CD) pipeline for the development of a Management System for Football Players, a detailed, structured approach is essential. This system aims to not only store basic information about football players but also to provide specialized, research-based treatment recommendations for injuries and medical conditions. To achieve this, a multifaceted development strategy incorporating various tools and methodologies is employed.

1. Source Code Repository

Objective: The primary goal is to develop a comprehensive management system designed to facilitate the provision of advice on treatment options for football players based on their specific injuries and medical conditions. The platform is envisioned to feature distinct interfaces and functionalities catered to different user roles.

Tools Utilized:  GitLab is designated as the central tool for project management. It serves as the repository for all developmental work, enabling efficient tracking and collaboration on code changes.  WhatsApp is leveraged for routine communication among team members, ensuring seamless coordination and exchange of ideas.

Actions: Developers engage in code development offline, committing their progress to the GitLab repository upon reaching significant milestones. This approach promotes structured development and version control.

2. Collection of Requirements

For Football Players: The system is required to maintain essential personal information, such as the player’s name, team affiliation, and age. Furthermore, it should provide access to treatment recommendations, derived from scholarly articles on post-injury care and research.

For Managers: Managers are granted comprehensive control over the system, including the capabilities to add, modify, and remove player profiles. They possess unrestricted access to all player data and treatment suggestions. Additionally, managers are empowered to manage the system’s back-end database, a crucial aspect of overall system maintenance and management.

3. Continuous Integration (CI)

Tools: A Virtual Box environment is utilized to simulate the operational setting of the website. This allows for thorough testing of the platform’s functionality in a controlled environment. Review & Approval: The system undergoes manual review and approval processes before being deployed into production. This includes the creation and utilization of mock accounts for managers, players, and general users to ensure comprehensive testing coverage.

3. Continuous Deployment (CD)

Feedback Mechanism: Post-testing, the identification of potential system issues is paramount. Team members responsible for testing communicate any discovered bugs or system shortcomings via the group chat on WhatsApp. This fosters an environment of continuous feedback and improvement.

Enhancement Discussions: Regular seminars and discussions are organized within the team to deliberate on ways to enhance the website and database. These sessions are critical for brainstorming improvements and implementing new features based on feedback and technological advancements.

Conclusion This academic approach to developing a CD pipeline for a Football Player Management System emphasizes the importance of structured development, meticulous requirement gathering, continuous integration and deployment, and an unwavering commitment to improvement. Through the employment of these strategies, the project aims to deliver a robust, efficient, and user-centric platform.

**Log-in page**

![Screenshot 2024-04-04 155150.png](uploads/1dde743387a4ecf56852d72998ba9385/Screenshot_2024-04-04_155150.png)

Page used in Usability testing:

![WhatsApp Image 2024-04-04 at 15.51.00_fd53cead.jpg](uploads/dd12091977374ab67ec63843be51173c/WhatsApp_Image_2024-04-04_at_15.51.00_fd53cead.jpg)For None-functional and usability test, we share the website to a number of users and asked them to use their imagination to play with the website, by the time of submission, no bug has been reported.



