# Introduction - (first lesson)
    > pipenv  init  	      &&   pipenv  shell
    > python -m venv my_env	  &&   my_env/Scripts/activate.bat
#### Django installation   
    > python -m pip install Django
    - django-admin --version
#### Create Django project   
    > django-admin startproject first_project
    - python manage.py runserver   (inside project folder)
#### Create App
    > python manage.py startapp first_app
#### Views       **(basics)
>- Views are the logic behind the application’s code. They are responsible for processing the request from the user, interacting with the models (db), and returning the data to the user.
>- RU: Views - это логика кода приложения. Они отвечают за обработку запроса от пользователя, взаимодействие с моделями (бд) и возврат данных пользователю. 
#### Urls        **(basics)
>- Urls are the paths that the user can take in the application. They are responsible for mapping the views to a specific path.
>- RU: Urls - это пути, которые пользователь может пройти в приложении. Они отвечают за сопоставление представлений с определенным путем.
#### Templates   **(basics)
>- Templates are the HTML files that are rendered by the views. They are responsible for the user interface of the application.
>- RU: Шаблоны - это HTML-файлы, которые отображаются представлениями. Они отвечают за пользовательский интерфейс приложения.


---
---
---
---
---

# Modals (second lesson)
- Modals are the database tables that are used to store the data of the application. They are responsible for the data storage of the application.
- RU: Модальные окна - это таблицы базы данных, которые используются для хранения данных приложения. Они отвечают за хранение данных приложения.