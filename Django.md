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
---

# Modals  &&  Admin-page  &&  Forms-(basics) 
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
        fields = ('first_name', 'last_name', 'age', 'email')   ||  '__all__'

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




---

# Templates (advanced)  &&  STATIC FILES

### Syntax of jinja2
```html
https://jinja.palletsprojects.com/en/3.1.x/templates/

{%  %}  =>  to write python code
{{  }}  =>  to write python variables
{#  #}  =>  to write comments

<!-- ----------------------------- -->
<!-- ----------------------------- -->
<!-- Blocks -->
{% block name %}
    ...
{% endblock %}
<!-- ----------------------------- -->
<!-- ----------------------------- -->
<!-- Datetime in jinja -->
{% now "Y-m-d" %}

<!-- ----------------------------- -->
<!-- ----------------------------- -->
<!-- Creating variables -->
{% with  variable_name = 'value' | filter-name %}
    <p>{{ variable_name }}</p>
{% endwith %}

```
Python filters:
1. *safe*     => {{ variable_name|safe }}  => is used to mark a string as safe, so that it is not escaped (safe means characters like <, >, and & are not escaped but rendered as is)
2. *escape*   => {{ variable_name|escape }}  => is used to escape a string (escape means characters like <, >, and & are escaped) 
3. *lower*    => {{ variable_name|lower }}  => is used to convert a string to lowercase
4. *upper*    => {{ variable_name|upper }}  => is used to convert a string to uppercase
5. *title*    => {{ variable_name|title }}  => is used to convert a string to titlecase
6. *length*   => {{ variable_name|length }}  => is used to get the length of a string
7. *striptags* => {{ variable_name|striptags }}  => is used to remove HTML tags from a string
8. *join*     => {{ variable_name|join:" " }}  => is used to join a list of strings with a separator
9. *default*  => {{ variable_name|default:"default value" }}  => is used to set a default value if the variable is not defined
10. *date*    => {{ variable_name|date:"Y-m-d" }}  => is used to format a date
11. *time*    => {{ variable_name|time:"H:i:s" }}  => is used to format a time
12. *random*  => {{ variable_name|random }}  => is used to get a random item from a list
13. *first*   => {{ variable_name|first }}  => is used to get the first item of a list
14. *last*    => {{ variable_name|last }}  => is used to get the last item of a list
15. *length_is* => {{ variable_name|length_is:"5" }}  => is used to check if the length of a string is equal to a value
16. *slice*   => {{ variable_name|slice:"1:3" }}  => is used to get a slice of a list
... and many more
https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters


```
<!-- ----------------------------- -->
<!-- ----------------------------- -->
<!-- For loop -->
{% for item in items %}
    <p>{{ item }}</p>
{% endfor %}
<!-- ----------------------------- -->
<!-- ----------------------------- -->
<!-- If statements -->
{% if condition %}
    <p>True</p>
{% elif condition %}
    <p>True</p>
{% else %}
    <p>False</p>
{% endif %}
<!-- ----------------------------- -->
<!-- ----------------------------- -->
<!-- Verbatim -->
{% verbatim %}
    <p>{{ this will not be interpreted as jinja code }}</p>
{% endverbatim %}
<!-- ----------------------------- -->
<!-- ----------------------------- -->
```

### 404-page
> 1. Debug mode must be set to False in settings.py
> 2. Set the ==>> ALLOWED_HOSTS = ['*'] in settings.py
> 3. TEMPLATES = [
>    { 'DIRS': [BASE_DIR / 'templates']  },
>]
> 4. Create a 404.html file in the templates folder of project folder


### base.html
>- We need the base.html for the following reasons:
>> RU: Нам нужен base.html по следующим причинам:
>-  To avoid repeating the same code in every page
>> RU: Чтобы избежать повторения одного и того же кода на каждой странице
>-  To have a consistent look and feel across the website
>> RU: Чтобы иметь единый внешний вид и ощущение на всем сайте
>-  To make it easier to make changes to the website
>> RU: Чтобы было легче вносить изменения на сайт

```html
<!-- base.html -->

<!-- imports -->
{% load static %} <!-- to load static files -->

<html>
<head>
    <title>{% block title %}{% endblock title %}</title>
    
    {% block css %}{% endblock css %}
</head>
<body>
    {% block content %}{% endblock content %}
    {% block scripts %}{% endblock scripts %}
</body>
</html>

...
### ------------------------- ### ----------------------------- ###
<!-- In other html files -->

{% extends 'base.html' %}

{% block title %}
    <title>My Website - Home</title>
{% endblock title %}

{% block css %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
{% endblock css %}

{% block content %}
    <h1>Welcome to my website!</h1>
    <p>Here's some content...</p>
{% endblock content %}

{% block scripts %}
    <script src="{% static 'js/script.js' %}"></script>
{% endblock scripts %}
```



### Include .html files in other html
> 1. Create a file with the html code that you want to include
>> RU: Создайте файл с html-кодом, который вы хотите включить
> 2. In the file that you want to include the html code, add the following code:
>> RU: В файле, в котором вы хотите включить html-код, добавьте следующий код
```
        {% include 'file_name.html' %}
```



### LOAD CSS
1. Put this into settings.py
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```
2. In your HTML template, load the static files by adding the following line at the top of the file:
```html
{% load static %}
<head>
<link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
</head>

<!-- TO IMPORT IMAGE -->
<img src="{% static 'path/to/image.png' %}" alt="Image description">
```


---

# Bootstrap  &&  Routing (intermediate)  &&  Details  &&  CRUD operations
### Bootstrap
1. Install bootstrap
```pip install django-bootstrap5```
2. Add bootstrap to INSTALLED_APPS in settings.py
```python
INSTALLED_APPS = [
    ...
    'django_bootstrap5',
]
```
3. Add the following code to the top of the base.html file
```html
{% load django_bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}
{% bootstrap_messages %}

<!-- ------------------------------------------- -->

<!-- To use bootstrap forms -->
{% load django_bootstrap5 %}
{% bootstrap_form form %}

```

### Routing
```html
   1. href="{% url 'name_of_url' %}" => to go to a url

   2. href="{% url 'name_of_url' variable %}" => to go to a url with a variable

   3. href="{% url 'name_of_url' variable1 variable2 %}" => to go to a url with multiple variables
```
---

# Querysets  &&  Models (advanced) 
---

```CRUD - operations```
>'*C*'reate
>'*R*'ead
>'*U*'pdate
>'*D*'elete


##### Create
```python
# Create a new object
new_object = ModelName.objects.create(field1=value1, field2=value2, ...)
ex: new_object = User.objects.create(first_name='John', last_name='Doe', age=30)
```

##### Read
```python
# Get all the objects
all_objs = ModelName.objects.all()
filtered_objs = ModelName.objects.filter(field1=value1, field2=value2, ...)
one_obj = ModelName.objects.get(field1=value1, field2=value2, ...)
...
```

##### Update
```python
# Update an object
obj.field1 = value1
obj.field2 = value2
obj.save()
```

##### Delete
```python
# Delete an object
obj.delete()
```


#### Chaining Querysets

```python
# Get all the objects that match the query and are ordered by the query
objs = ModelName.objects.filter(field1=value1, field2=value2, ...).order_by('field1', 'field2', ...)

# Get the first object that matches the query
obj = ModelName.objects.filter(field1=value1, field2=value2, ...).first()

# Get an object by chain-filtering
# Double underscore (__) is used to chain filters
objs = ModelName.objects.filter(user__name__endswith='John')
objs = ModelName.objects.filter(name__contains='John').filter(age__gt=30)
objs = ModelName.objects.filter(name__startswith='John').filter(age__gt=30).first()
objs = ModelName.objects.filter(name__in=[names]).filter(age__lt=30)
```

#### Exclude
```python
# Get all the objects that don’t match the query
objs = ModelName.objects.exclude(field1=value1, field2=value2, ...)

```

#### F() = is used to compare two fields
```python
from django.db.models import F

F() allows us to compare two fields in a model.


# Get all the objects where field1 is greater than field2
objs = ModelName.objects.filter(field1__gt=F('field2'))
ex: 
    ice_creams = IceCream.objects.filter(sugar__lt=F('fat'))
    # This will return all the ice creams where the sugar is less than the fat

# Get all the objects where field1 is greater than field2 and field3 is less than field4
objs = ModelName.objects.filter(field1__gt=F('field2'), field3__lt=F('field4'))
```

#### Q() = is used to make complex queries
```python
from django.db.models import Q

Q means OR and ~Q means NOT

# Q
# Get all the objects where field1 is greater than field2 or field3 is less than field4
objs = ModelName.objects.filter(Q(field1__gt=F('field2')) | Q(field3__lt=F('field4')))
objs = ModelName.objects.filter(Q(field1__gt=F('field2')) | Q(field3__lt=F('field4'))).order_by('field1', 'field2', ...)


# ~Q
# Get all the objects where field1 is greater than field2 and field3 is less than field4
objs = ModelName.objects.filter(~Q(field1__gt=F('field2')) & Q(field3__lt=F('field4')))
objs = ModelName.objects.filter(~Q(field1__gt=F('field2')) & Q(field3__lt=F('field4'))).order_by('field1', 'field2', ...)
```


#### ORM and Aggregation
ORM  =>  Object-Relational Mapping
It allows us to query the database using object-oriented programming.
It is useful on large databases rather than small ones as it can get the results faster.

Suppose you have a Book model with fields *title*, *author*, and *price*. You want to find the average price of all books, the count of all books, the minimum price of all books, the maximum price of all books, and the total price of all books.

Here's how you can use the aggregate function to achieve this:
```python
from django.db.models import Avg, Count, Min, Max, Sum
from myapp.models import Book

# Get the average price of all books
avg_price = Book.objects.all().aggregate(Avg('price'))

# Get the count of all books
book_count = Book.objects.all().aggregate(Count('id'))

# Get the minimum price of all books
min_price = Book.objects.all().aggregate(Min('price'))

# Get the maximum price of all books
max_price = Book.objects.all().aggregate(Max('price'))

# Get the total price of all books
total_price = Book.objects.all().aggregate(Sum('price'))
```

This will return a dictionary with the calculated values for each query. For example, **avg_price** will be a dictionary with a single key-value pair, where the key is '**price__avg**' and the value is the average price of all books. Similarly, **book_count** will be a dictionary with a single key-value pair, where the key is '**id__count**' and the value is the count of all books.


#### Custom Manager
```python
class InStockManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(in_stock=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    objects = models.Manager()  # The default manager
    in_stock_objects = InStockManager()  # Custom manager

    def __str__(self):
        return self.title

### ------------------------- ### ----------------------------- ###
### VIEWS
### ------------------------- ### ----------------------------- ###

from myapp.models import Book

# Get all books
all_books = Book.objects.all()

# Get only books that are currently in stock
# RU: Получить только книги, которые в настоящее время есть в наличии
in_stock_books = Book.in_stock_objects.all()
```




#### Overriding existing methods and adding new methods
```python
import json
class Book(models.Model):
    ...
    # We don't use json-field because it is not supported by all databases
    
    all_json_data = models.TextField(default='{}')

    def get_data(key=None, detault=None):
        data = json.parse(self.all_json_data)
        default = default or f'Key {key} does not exist'
        if (key):
            return data.get(key, default)
        return data

    def set_data(data):
        self.all_json_data = json.dumps(data)
        self.save()

    def update_data(data):
        old_data = self.get_data()
        old_data.update(data)
        self.set_data(old_data)
        self.save()
    

    def save(self, *args, **kwargs):
        # Do something
        # ex: self.title = self.title.upper()
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def delete(self, *args, **kwargs):
        # Do something
        # ex: self.children.all().delete()
        super().delete(*args, **kwargs)  # Call the "real" delete() method.

    
```
#### Integrity checks and custom Exceptions
Integrity checks are used to ensure that the data is consistent and correct. For example, if we have a Book model with a field *title* that is required, we can use an integrity check to ensure that the title is not empty.

```python
from django.db import IntegrityError

class Book(models.Model):
    ...

    def save(self, *args, **kwargs):
        if not ...
            raise IntegrityError(f'...')
        super().save(*args, **kwargs)  # Call the "real" save() method.
```



## Updating db with migrations
To create an empty migration file 
```python manage.py makemigrations --empty yourappname```


Then we update the migration file like this:
```python
from django.db import migrations

def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Person = apps.get_model("yourappname", "Person")
    for person in Person.objects.all():
        person.name = f"{person.first_name} {person.last_name}"
        person.save()


class Migration(migrations.Migration):
    dependencies = [
        ("yourappname", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
```


#


#
