# drf-api
"drf-api"" is the backend service used by the [Connect](https://github.com/TiagoMA90/connect) platform.
The deployed DjangoRESTFramework API can be found [here](https://djangorestframework-api-38c4a098777a.herokuapp.com/)

# Purpose of the API:
To serve as the Back bone for the Front-end, by posting and getting data from endpoints and to perform Create, Read, Update and Delete operations to objects entered by Users via Front-end.

## Planning & Agile:
This [project](https://github.com/users/TiagoMA90/projects/10) was planned using Agile methodology and MoSCoW prioritization.

For this purpose, the project was illustrated by [9 initial Milestone](https://github.com/TiagoMA90/drf-api/milestones) entitled "Profiles", "Posts", "Likes", "Comments", "Followers", "Reviews", "walls", "Contacts" and "Reports"  providing the developer with the freedom to accomplish all issues/tasks flexibly before dates deadline set to November. The Milestones were broken according to their components name.

Throughout the development process, new milestones were added, where tasks started from "Todo," progressing to "In Progress," and finally "Done". The issues were assigned to the sole developer and labeled as "could-have," "should-have,", "must-have" and "won't-have".

<img src="readme/SampleAgile.png" alt="Sample Agile">

In order of priority, with [62 closed User Stories](https://github.com/TiagoMA90/drf-api/issues?q=is%3Aissue+is%3Aclosed), the Project has:

Must-Have:
- Models, Views, Serializers, Urls for "profiles/posts/comments/likes/reviews/walls"
- Set Up and Deployment
- View Users Profiles (Profiles)
- Profiles Permissions (Profiles)
- View Posts (Posts)
- Create a Post (Posts)
- Post Permissions (Posts)
- View Comments (Comments)
- Create a Comment (Comments)
- Like Permissions (Likes)
- Report Premissions (Reports)
- View Contacts (Contacts)
- Reviews Permissions (Reviews)
- Create a Review (Reviews)
- Wall posts Permissions (Walls)
- Create a Wall post (Walls)

Should-Have:
- Models, Views, Serializers, Urls for "followers/reports/contacts
- View Users Detail Profile (Profile)
- Update User Profile (Profile)
- Delete User Profile (Profile)
- Filter Posts (Posts)
- Update my Post (Posts)
- Like a Post (Posts)
- Comment on a Post (Posts)
- View Comments Details (Comments)
- Update my Comment (Comment)
- Delete my Comment (Comment)
- View Like (Likes)
- Like/Unlike a Post (Likes)
- View Like Details (Likes)
- View Followers (Followers)
- Follow a User (Followers)
- Unfollow a User (Followers)
- View Follower Details
- Create a Report (Reports)
- View Report Details (Reports)
- Create a Contact (Contacts)
- Contact Premissions (Admin)(Contacts)
- View Contacts Details (Admin)(Contacts)
- View Reviews Details (Reviews)
- Update my Review (Reviews)
- View Wall posts Details (Walls)
- Update my Wall post (Walls)

Could-Have:
- Models, Views, Serializers, Urls for "likes"
- Search for Posts (Posts)
- View Posts Details (Posts)
- Delete a Contact (Admin)(Contacts)
- Update a Contact (Admin)(Contacts)

Wont-Have:
- Remove a Follower (Followers)
- Update my Report (Reports)
- Delete my Report (Reports)
- Delete my Review (Reviews)
- Delete my Wall post (Walls)

The issues were closed and the milestones subsequently too.

## Relationship Diagram
The relationship diagram between models from an individual perspective can be best defined as follows:

- The [Profile](https://djangorestframework-api-38c4a098777a.herokuapp.com/profiles/) flaunts the owner(OneToOne), image(ImageField), content(TextField), name(CharField), created_at(DateTimeField) and updated_at(DateTimeField)
- A [Post](https://djangorestframework-api-38c4a098777a.herokuapp.com/posts/) created by a User Profile, features the owner(ForeignKey), created_at(DateTimeField), updated_at(DateTimeField), title(CharField), content(TextField), image(ImageField) and image_filter(CharField) once submited
- The [Comments](https://djangorestframework-api-38c4a098777a.herokuapp.com/comments/) model takes a similar approach, inheriting the post(ForeignKey) and owner(ForeignKey), it displays the content(TextField), created_at(DateTimeField), updated_at(DateTimeField) of the comment
- The [Like](https://djangorestframework-api-38c4a098777a.herokuapp.com/likes/) marked by the owner(ForeignKey), post(ForeignKey) and created_at(DateTimeField)
- The [Follower](https://djangorestframework-api-38c4a098777a.herokuapp.com/followers/) defined by owner(ForeignKey), followed(ForeignKey), created_at(DateTimeField)
- Then the [Report](https://djangorestframework-api-38c4a098777a.herokuapp.com/reports/) functionality enlists a tuples for REASON_CHOICES, followed by the reporter(ForeignKey) and post(ForeignKey), reason(CharField), description(TextField) and created_at(DateTimeField)
- The [Contact](https://djangorestframework-api-38c4a098777a.herokuapp.com/contacts/) form finally isolated makes use of the name(CharField) and email(EmailField) for external users, subject(Charfield), message(TextField), created_at(DateTimeField).

Under Barker's notation. One/Many Users can create multiple Profiles, which can then create many Posts. Many Comments can be created in many Posts by one/many Profiles. One Likes/Unlikes can be created in many Posts by one/many Profiles. Many Reports can be created on many Posts by one/many Profiles. One/Many Profiles can follow/unfollow many Profiles. Contacts should be considered an isolated model as it is accessible by anyone, ergo many Users.

<img src="readme/DiagramRelationship.png" alt="Models Diagram">

## Methodology CRUD
When performing CRUD (Create, Retrieve, Update, Delete) function based views, the following methods were used to manipulate the table in the database.

For such, to the subsequent endpoints:
/profiles/, /posts/, /comments/, /likes/, /followers/, /reviews/, /walls/, /reports/, /contacts/

- POST - Used to create an object to a list of (endpoint)
- GET - Used to retrieve series of objects from a list of (endpoint)

Singularly, for the same endpoints past the primary keys:
/profiles/int:pk/, /posts/int:pk/int:pk/, /comments/int:pk/, /likes/int:pk/, /followers/int:pk/, /reviews/int:pk/, /walls/int:pk/, /reports/int:pk/, /contacts/int:pk/

- GET - Used to view a single object in a list or (endpoint)
- PUT - Used to update a single object in a list of (endpoint)
- DELETE - Used to delete an existant single object from a list of (endpoint)

Users can then:
- CRUD Profiles
- CRUD Posts
- CRUD Comments
- CRUD Likes
- CRUD Followers
- CRU Reviews
- CRU Walls
- CR Reports
- CR Contacts

## Features and Functionality for Superusers

As a Superuser one has the ability to perform the following via the [admin panel](https://djangorestframework-api-38c4a098777a.herokuapp.com/admin/):
- CRUD Posts
- CRUD Comments
- CRUD Profiles
- CRUD Reviews
- CRUD Walls
- CRUD Contacts
- CRUD Reports
- Change Passwords
- Promote users to Superuser

<img src="readme/AdminPanel.png" alt="Admin Panel (local)">

## Manual Testing
Manual Testing for the overall functionality of the API was performed by entering dummy data in the backend both via Backend-and Front-end.
All data is CRUDed accordingly.

CI Python Linter was also used in parallel with the development of the API, to keep the code free of errors.

The Code has not exhibited apparent errors after consecutive tests and corrections throughout the development. Test Commits were exectuted in attempts to test the responsivness with the Front and the deployed Back-end.

<img src="readme/CIPythonLinter.png" alt="CI Python Linter">

## Installed Python Packages
The following packages were installed when developing this project:
To install, the following command ran: ```pip install``` ...
- ```Pillow==8.2.0``` <- Python Imaging Library
- ```psycopg2==2.9.6``` <- PostgreSQL adapter for Python
- ```cloudinary==1.25.0``` <- Cloudinary - cloud-based image and video host
- ```dj-database-url==0.5.0``` <- Utility library for Django
- ```dj-rest-auth==2.1.9``` <- Authentication functionality for DjangoRESTFramework-based APIs
- ```Django==3.2.4``` <- Python web framework
- ```django-allauth==0.44.0``` <- Extension for Django to a customizable authentication system
- ```django-cloudinary-storage==0.3.0``` <- Cloudinary - Backend storage for static media files
- ```django-cors-headers==3.7.0``` <- Middleware Cross-Origin Resource Sharing (CORS)
- ```django-filter==2.4.0``` <- Package to simplify filtering QuerySets
- ```djangorestframework==3.12.4``` <- Toolkit for building Web APIs
- ```djangorestframework-simplejwt==4.7.2``` <- Extension that provides JSON Web Token (JWT) authentication
- ```gunicorn==20.1.0``` <- WSGI HTTP server for running Python web applications
- ```PyJWT==2.1.0``` <- Library for working with JSON Web Tokens (JWT)

## Package Dependencies
- asgiref==3.3.4
- cryptography==3.4.8
- oauthlib==3.1.1
- python3-openid==3.2.0
- pytz==2021.1
- requests-oauthlib==1.3.0
- sqlparse==0.4.1
- urllib3==1.26.15

# Development & Deployment
The project was developed using GitHub and GitPod platforms...
- Navigate to: "Repositories" and create "New".
- Mark the following fields: ✓ Public ✓ Add a README file.
- Select template: "Code-Institute-Org/python-essentials-template".
- Add a Repository name: "drf-api".
- ...and create Repository.

... and suffered various executions using the inbuild Terminal.

For Commits on this project, the following commands ran:
- ```git add .``` <- Stages before commiting.
- ```git commit -m "written imperative declaration"``` <- Declares changes and updates.
- ```git push``` <- Push all updates to the GitHub Repository.

To run the server locally (Debug = True), the following command ran:
- ```python manage.py runserver``` <- Loads the website on the in-built Terminal.

During development migrations to the database were made.
To make migrations the following commands ran:
- ```python manage.py makemigrations``` <- Creates a new database migration
- ```python manage.py migrate``` <- Applies pending migrations

To create or update Requirements.txt file the following commands ran:
- ```pip3 freeze --local > requirements.txt```  <-Runs the req.
- ```pip install -r requirements.txt``` <- Install req.

To create a Superuser the following command ran (from Heroku terminal): 
- ```python manage.py createsuperuser``` (username->email->password1->password2) <- Creates a Superuser

To create a new Django project, in the currenct directory, the followig command ran:
- ```django-admin startproject NAMEOFTHEPROJECT .``` <- Starts the project

To create the app the following command ran:
- ```python3 manage.py startapp NAMOFTHEAPP``` <- Creates a folder for the app withing the project
- 
The website is being hosted and deployed on Heroku:
- After creating an Heroku Free account, and applying for Student Pack
- Navigate to: "Create new app" add a unique name "djangorestframework-api" and select "Europe" region. Click "Create App"
- Head over to "Settings" tab and apply the respective config VARs
- Move to "Deploy" section and select "Github" method"
- From here search for the repository name "connect", from the GitHub account.
- Hit "Connect" and "Enable Automatic Deploys" to keep the the repository in parallel to Heroku.
- Manually "Deploy Main Branch".
- Upon successful deployment, retrieve the link for the mock terminal.
- The live app can be found [here](https://djangorestframework-api-38c4a098777a.herokuapp.com/).

## Languages & Technologies
- Django REST Framework (Python Framework - API)

## Other forms of development
- [CI Python Linter](https://pep8ci.herokuapp.com/) - CI Python testing tool
- [Diagrams](https://app.diagrams.net/) - Diagram set up
- [Github](https://github.com/) - Host for the repository
- [Gitpod](https://gitpod.io/) - Code editor
- [ElephantSQL](https://www.elephantsql.com/) - Database
- [Cloudinary](https://cloudinary.com/) - Static & Media host
- [Heroku](https://id.heroku.com/) - Cloud platform/Host the live project

## Credits
The following sources and references were resorted for the creation of this website:
- The lessons and tutorials provided by Code Institute, on the final module entitled "Django REST Framework" for the 'Advanced Front-End' specialization
- The Tutor team provided by Code Institutes Student Support
- Slack(#project-portfolio-5-advanced-frontend) as a solution platform for broken code and guidance on how to procceed to blockades
