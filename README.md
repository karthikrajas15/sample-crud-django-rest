This contains sample CRUD operation with python Django REST API. Its a simple task manager application. You can add task, update the task, read and delete the task. 

1) create virtual environment using the following command
	python3 -m venv /path/vishgyanaenv
2) After create virtual environment activate it using the command
	source /path/vishgyanaenv/bin/activate
3) install the python packages which is in requirement.txt file using the command
	pip install -r /path/requirement.txt
Now the environment is ready, you can run the code using python manage.py runserver
open the ip link with you browser.

4) Set up postgresql in your machine
5) Create Database


After install requirement.txt use following commands to run the project

1. update the postgres database name and password in settings file
2. cd /path/vishgyan/app_config
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver


After project run successfully use the following urls in postman to check the appropriate results

1. localhost:8000/task/user-registration/
2. localhost:8000/task/user-login/
3. localhost:8002/task/task-create/
4. localhost:8000/task/task-update/<int:id>/
5. localhost:8002/task/task-delete/<int:id>/
