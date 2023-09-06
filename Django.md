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

# models 
- models.CharField      - a string of characters
- models.URLField       - a string that has to be a valid URL format
- models.IntegerField   - a whole number
- models.DateField      - a date field
- models.DateTimeField  - a date and time field
- models.BooleanField   - a True/False field
- models.EmailField     - a field that checks that the input is a valid email address
- models.FileField      - a file-upload field
- models.ImageField     - an image-upload field
- models.ForeignKey     - a field used to specify a one-to-many relationship
- models.ManyToManyField - a field used to specify a many-to-many relationship
- models.OneToOneField  - a field used to specify a one-to-one relationship

#### Create superuser
    > python manage.py createsuperuser

#### To get the sql info in the terminal
    > python manage.py sqlmigrate app_name migration_name

#### To register the app in the admin.py
```python
    from django.apps import apps
    from django.contrib import admin

    app = apps.get_app_config('users')

    for model_name, model in app.models.items():
        admin.site.register(model)
```

#### Create and Get Objects inside views.py
- We can do this by importing the models from the first_app folder.
- RU: Мы можем сделать это, импортировав модели из папки first_app.
```python
from django.shortcuts import render
from first_app.models import *

def get_webpage(request):
    webpages_list = Webpage.objects.order_by('date')
    context = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context)

def create_webpage(request):
    webpage = Webpage.objects.get_or_create(topic=topic, name=name, url=url)[0]
    return webpage

### ---------------------------------- ### ---------------------------------- ###
# modal_name.object.all()       => returns all the objects in the database

# -----------------------

# modal_name.object.get()       => returns the object that matches the query
#   ex: modal_name.object.get(id=1)  => returns the object with id=1

# -----------------------

# modal_name.object.filter()    => returns a list of objects that match the query
#   ex: modal_name.object.filter(id=1)  => returns a list of objects with id=1

# -----------------------

# modal_name.object.order_by()  => returns a list of objects that are ordered by the query
#   ex: modal_name.object.order_by('date')  => returns a list of objects that are ordered by the date

# -----------------------

# modal_name.object.get_or_create()  => returns the object that matches the query, if it doesn’t exist it creates it

# -----------------------

# modal_name.object.update_or_create()  => returns the object that matches the query, if it doesn’t exist it creates it

# -----------------------

# modal_name.object.delete()    => deletes the object that matches the query

# -----------------------

# modal_name.object.count()     => returns the number of objects that match the query

# -----------------------

# modal_name.object.first()     => returns the first object that matches the query

# -----------------------

# modal_name.object.last()      => returns the last object that matches the query

# -----------------------

# modal_name.object.exists()    => returns True if the object exists

# -----------------------

# modal_name.object.distinct()  => returns a list of objects that are distinct

# -----------------------

# modal_name.object.values()    => returns a list of dictionaries with the values of the objects

# -----------------------

# modal_name.object.values_list()  => returns a list of tuples with the values of the objects

# -----------------------

# And the difference between them is that values() returns a dictionary and values_list() returns a tuple.
#   ex: modal_name.object.values('name', 'url')  => returns a list of dictionaries with the name and url of the objects
#   ex: modal_name.object.values_list('name', 'url')  => returns a list of tuples with the name and url of the objects

# -----------------------

# modals_name.object.filter().order_by().values()  => returns a list of dictionaries with the values of the objects that match the query and are ordered by the query
```

#### Forms (simple)
- forms.py
```python
class UserForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='Email', max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', 'email')

### ------------------------- ### ----------------------------- ###
# IN VIEWS.PY
from first_app.forms import UserForm

def index(request):
    form = UserForm()  # initialize the form
    if request.method == 'POST':   # if the form is submitted
        form = UserForm(request.POST) # initialize the form with the data from the request
        if form.is_valid():  # if the form is valid
            form.save(commit=True) # save the form to the database
            # commit=False means that we will not save the form to the database yet.
            # This is useful if we want to add or change something before saving it.
            return index(request) # call the same view function/page again
        else:
            print('ERROR FORM INVALID')
    return render(request, 'page_for_form.html', {'form': form})

### ------------------------- ### ----------------------------- ###
# IN HTML

<form method="POST">
    {% csrf_token %}
    # csrf_token is a security feature that prevents Cross-Site Request Forgery (CSRF) attacks.
    # CSRF attacks are a type of malicious attack where unauthorized commands are performed on behalf of an authenticated user.
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>

form.as_p       => means that the form will be rendered as a paragraph
form.as_table   => means that the form will be rendered as a table
form.as_ul      => means that the form will be rendered as a list
form.as_div     => means that the form will be rendered as a div
```