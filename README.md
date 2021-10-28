# Reviewer

>[HWaruguru](https://github.com/HWaruguru)  
  
# Description  
This project allows users to post their projects for other users to rate according to design, usability and content 
##  Live Link  
 Click [View Site]()  to visit the site
   
## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/HWaruguru/Reviewer.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Reviewer pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual
```  
```bash 
source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations reviewer
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 ### Api Endpoints
 * https://hanreviewer.herokuapp.com/api/project/
 * https://hanreviewer.herokuapp.com/api/profile/
 * https://hanreviewer.herokuapp.com/
 
 
## Technology used  
  
* [Python3.9](https://www.python.org/)  
* [Django 3.2.8](https://docs.djangoproject.com/en/3.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [hannah.waruguru8@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/HWaruguru/Reviewer/blob/master/LICENSE)  
* Copyright (c) 2021 **Hannah Waruguru**