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
avg_price = Book.objects.aggregate(Avg('price'))

# Get the count of all books
book_count = Book.objects.aggregate(Count('id'))

# Get the minimum price of all books
min_price = Book.objects.aggregate(Min('price'))

# Get the maximum price of all books
max_price = Book.objects.aggregate(Max('price'))

# Get the total price of all books
total_price = Book.objects.aggregate(Sum('price'))
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
        data = json.loads(self.all_json_data)
        if (key):
            default = default or f'Key {key} does not exist'
            return data.get(key, default)
        return data

    def set_data(data):
        self.all_json_data = json.dumps(data)
        self.save()

    def update_data(new_data):
        old_data = self.get_data()
        old_data.update(new_data)
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
    User = apps.get_model("users", "User")
    for user in User.objects.all():
        user.name = f"{user.first_name} {user.last_name}"
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ("yourappname", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
```


# Forms (advanced)  &&  File upload  &&  Data validation &&  TinyMCE

#### Simple forms
```python
# forms.py

from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='Email', max_length=100)
```

#### Django messages
```python
from django.contrib import messages
SYNTAX:  messages.mode(request, 'message')
EXAMPLE: messages.success(request, f'Hello world')
```
And in HTML
```html
    <div class="container" id="messages">
       {% bootstrap_messages %}
    </div>

    <!-- Make it disappear after a while -->
    <script>
      setTimeout(function () {
        var messages = document.querySelectorAll('#messages')
        messages.forEach(function (message) {
          message.remove()
        })
      }, 5000)
    </script>
```

#### Forms with widgets

Widgets are used to customize the look and feel of the form fields. For example, we can use a TextInput widget to change the input field from a text field to a password field.

```python

from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

### ------------------------- ### ----------------------------- ###
# WITH CHOICES FIELD
from django import forms

CHOICES = (
    ('1', 'First Choice'),
    ('2', 'Second Choice'),
    ('3', 'Third Choice'),
)
class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
```

#### Uploading Images
First we need to install Pillow
```pip install Pillow```

Then we need to add the following code to settings.py
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Then we need to add the following code to urls.py
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Then we need to add the following code to models.py
```python
from django.db import models

class User(models.Model):
    ...
    image = models.ImageField(upload_to='images/', default='images/default.png')
```

Then we need to add the following code to forms.py
```python
from django import forms

class UserForm(forms.Form):
    ...
    image = forms.ImageField(label='Image', widget=forms.FileInput(attrs={'class': 'form-control'}))
```

Then in views.py
```python
...
def index(request):
    ...
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
    ...
...
```

Then we need to add the following code to index.html
```html

<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>

```

Then we should decrease the size of the image
```python
from PIL import Image

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    img = Image.open(self.image.path)
    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)
```



#### Data validation
clean methods are used to validate the data. For example, we can use the clean_first_name method to check if the first name is empty. Or, use just clean to check if the form is valid.

```python

def clean(self):
    cleaned_data = super().clean()
    first_name = cleaned_data.get('first_name')
    last_name = cleaned_data.get('last_name')
    age = cleaned_data.get('age')
    email = cleaned_data.get('email')
    choice = cleaned_data.get('choice')

    if not first_name:
        raise forms.ValidationError('First name is required')
    if not last_name:
        raise forms.ValidationError('Last name is required')
    if not age:
        raise forms.ValidationError('Age is required')
    if not email:
        raise forms.ValidationError('Email is required')
    if not choice:
        raise forms.ValidationError('Choice is required')
    return cleaned_data
```

```python
from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('First name is required')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError('Last name is required')
        return last_name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if not age:
            raise forms.ValidationError('Age is required')
        return age

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required')
        return email

    def clean_choice(self):
        choice = self.cleaned_data.get('choice')
        if not choice:
            raise forms.ValidationError('Choice is required')
        return choice
```








#### TinyMCE
`pip3 install django-tinymce4-lite`


Next is open your setting.py and add ‘tinymce’ on your INSTALLED_APPS.
And, put this into settings.py
```python
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}
```
Next is open your urls.py and add this code.
```python
...
path('tinymce/', include('tinymce.urls')),
...
```

Next is open your models.py and add this code.
```python
from tinymce.models import HTMLField

class Post(models.Model):
    ...
    content = HTMLField()
```

Next is open your admin.py and add this code.
```python
from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["post_title", "post_date"]}),
        ("Content", {"fields": ["post_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Post, PostAdmin)
```


Next is open your index.html and add this code.
```html
...
<p>{{ object.html_field|safe }}</p>
...
```

Next is our forms.py and add this code.
```python
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    ...
    post_content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    ...
```



# Sign - In/Out   &&   Profile🧑🏻‍🏫  &&   User-related-updates 

#### UserCreationForm
```python
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
   email = forms.EmailField(...)

   class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')


### ------------------------- ### ----------------------------- ###
# VIEWS
### ------------------------- ### ----------------------------- ###
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


### ------------------------- ### ----------------------------- ###
# HTML
### ------------------------- ### ----------------------------- ###

We can use the following code to check if the user is logged in or not
{% if user.is_authenticated %}
    <p>Logged in</p>
{% else %}
    <p>Not logged in</p>
{% endif %}

```

#### LoginView and LogoutView
We can use these to create login and logout views. 
We can also use these to create login and logout urls.

```python
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    ...
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    ...
]
```
and in settings.py we must put these so that it knows where to redirect after login and logout
```python
LOGIN_REDIRECT_URL = 'home_page'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
```

#### @login_required decorator
We can use this decorator to make sure that only logged in users can access a view.
```python
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    ...
```

#### Create profile
```python
# Models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     ...
# ...

# Signals

import logging
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
log = logging.getLogger(__name__)  # Get an instance of a logger


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    This function will be called every time a new user is created.
    It will create a new profile for the user.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """This function will be called every time a user is saved."""
    instance.profile.save()
    log.info(f"UserProfile has been created for {instance.username}")


# apps.py
from django.apps import AppConfig
class UsersConfig(AppConfig):
    ...

    # We have to import the signals here so that they are registered 
    def ready(self):
        import users.signals
```




#### Update profile
```python

# Forms
import all imports

class UserUpdateForm(UserCreationForm):
    email = forms.EmailField(...)
    
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)


# Views
all imports

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
```








# Class Based Views (intermediate)
Class-based views are an alternative to function-based views. They provide a lot of functionality out of the box, and they are easier to extend and customize.

#### General rulses of CBV
> 1. Each view class must inherit from a base view class
> 2. Each view does something and returns an HttpResponse object
> 3. Each view has a get method and/or a post method
> 4. Each view has a template_name attribute that specifies which template to use and/or a model attribute that specifies which model to use
> 5. Each view has a get_context_data method that returns a dictionary of context data to be used in the template
> 6. Each view does only one thing and does it well and has a descriptive name that describes what it does

`SYNTAX`
```python
from django.views.generic import ...

class ViewName(...):
    template_name = 'template_name.html' 
    # it is better to use this because it is more flexible 
    #
    model = ModelName # optional and not needed for all views

    def get(self, request, *args, **kwargs):
        # Do something
        return HttpResponse(...)

    def post(self, request, *args, **kwargs):
        # Do something
        return HttpResponse(...)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Do something
        return context
```

#### TemplateView
```python
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome to my website!'
        return context
```

#### ListView
TemplateView is used when you want to display a template without any model data. It's typically used for static pages like the homepage, about page, or contact page. You can override the template_name attribute to specify which template to use, and you can also override the get_context_data method to add additional context data to the template.

ListView, on the other hand, is used when you want to display a list of objects from a model. It automatically generates a queryset based on the model you specify, and it uses a default template to display the list of objects. You can override the model attribute to specify which model to use, and you can also override the template_name attribute to use a custom template.
```python
from django.views.generic import TemplateView, ListView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Books.objects.all()

### ------------------------- ### ----------------------------- ###
# post_list.html
...
    {% for post in object_list %}
        <p>{{ post.title }}</p>
    {% endfor %}
...
```

#### DetailView
DetailView is a class-based view in Django that is used to display the details of a single object from a model. It's typically used when you want to display more information about an object than just a list of objects.
```python
from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs['pk'])
```
In urls.py
```python
    path("book_details/<int:pk>", BookDetailsView.as_view(), name="book_details"),
```

```html
<h1>{{ object.title }}</h1>
<p>{{ object.body }}</p>
```

#### CreateView
It's used when we want to allow users to create new objects in our application.
```python
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm # This lets to use the form that we created inside templates
    template_name = 'post_form.html'
    success_url = '/posts/'
```

#### UpdateView
It's used when we want to allow users to update existing objects in our application.
```python
from django.views.generic import UpdateView
from .models import Post
from .forms import PostForm

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = '/posts/'
```

#### DeleteView
It's used when we want to allow users to delete existing objects in our application.
```python
from django.views.generic import DeleteView
from .models import Post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/posts/'
```

#### FormView
It's used when we want to display a form to the user and process the form data in the same view.
```python
from django.views.generic import FormView
from .forms import ContactForm

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
```

#### RedirectView
It's used when we want to redirect the user to a different URL.
```python
from django.views.generic import RedirectView

class HomeRedirectView(RedirectView):
    url = '/home/'
```

#### ListView with pagination
```python
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 5
```
```html
{% if is_paginated %}
    <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.previous_page_number }}" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
            {% else %}
                <li class="page-item disabled">
                    <a class="page-link" href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
            {% endif %}
            {% for i in paginator.page_range %}
                {% if page_obj.number == i %}
                    <li class="page-item active">
                        <a class="page-link" href="?page={{ i }}">{{ i }}</a>
                    </li>
                {% else %}
                    <li class="page-item">
                        <a class="page-link" href="?page={{ i }}">{{ i }}</a>
                    </li>
                {% endif %}
            {% endfor %}
            {% if page_obj.has_next %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.next_page_number }}" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
            {% else %}
                <li class="page-item disabled">
                    <a class="page-link" href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
            {% endif %}
        </ul>
    </nav>
{% endif %}
```




# Middleware and Sessions (advanced)

#### Middleware
- Middleware in django is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output. **In other words, it is a better way to modify the request and response objects in Django.**

- To create a middleware in Django, you can follow these steps:
  1. Create a new Python module in your Django project's directory, for example middleware.py.
  2. Define a class that implements the middleware functionality you need. The class should have a __init__ method that takes a get_response argument, which is a callable that takes a request and returns a response. The class should also have a __call__ method that takes a request and returns a response.
  3. Implement the middleware functionality in the __call__ method. This could include tasks such as modifying the request or response, performing authentication, or logging.
  4. Add the middleware class to the MIDDLEWARE setting in your project's settings.py file. The order of middleware classes in the list matters, so make sure to add your middleware in the appropriate position.

```python
def print_time_taken(request, response):
    time_taken = time.time() - request.start_time
    print(f'Time taken: {round(time_taken, 5)} seconds')
    return response


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the view function name

       

        # Code to be executed for each request before
        print('I am before the view is called')

        request.start_time = time.time()
        response = self.get_response(request)
        response = print_time_taken(request, response)
        # Do something after the view is called

        view_name = request.resolver_match.view_name
        if view_name is not None:
            print(f'I am after the {view_name} view is called')

        return response
```
And here's how you would add this middleware to the MIDDLEWARE setting in your settings.py file:
```python
MIDDLEWARE = [
    ...
    'myapp.middleware.MyMiddleware',
    ...
]
```
Note that path.to.MyMiddleware should be replaced with the actual path to your middleware class.


#### Sessions
To use sessions in Django, you need to enable session support in your project's settings.py file by adding `'django.contrib.sessions.middleware.SessionMiddleware'` to the MIDDLEWARE setting. Once session support is enabled, you can use the request.session object to store and retrieve data in the session.
```python
# views.py
from django.shortcuts import render

def my_view(request):
    # Get the value of the 'my_key' key from the session, or return None if it doesn't exist
    my_value = request.session.get('my_key')

    # Set the value of the 'my_key' key in the session
    request.session['my_key'] = 'my_value'

    return render(request, 'my_template.html', {'my_value': my_value})
```
<br>
<br>
<br>

# 📚Django-allauth 
```pip install django-allauth```
<br>
<br>

### Configuration
First of all we need to configure our settings.py file
```python
# 1-Click Button Generate a New Client Secret;
# 2-fill in the blanks in .settings.py:
# 3-Application name:  Django Demo Auth
# 4-Homepage URL: https://127.0.0.1:8000/
# 5-Authorization callback URL:  https://127.0.0.1:8000/accounts/github/login/callback
# 6-Goto to your app login (http://127.0.0.1:8000/) and authorize app.
```

```python
# INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    ...
]
# =============================================================
# And we need to set SITE ID
SITE_ID = 1
# This helps allauth to know which site we are using and which site to redirect to after login
# =============================================================
# AUTHENTICATION_BACKENDS
# It is needed to allow this site to use allauth with the default authentication system of Django
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
# ============================================================= 
# Then we should specify context processors
# They are used to add context variables to all templates
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.request',
                ...
            ],
        },
    },
]
# =============================================================
SOCIALACCOUNT_PROVIDERS = {
    # site for creating google auth service https://console.cloud.google.com/
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '...',
            'secret': '...',
            'key': ''
        }
    },
    # ============================================================================
    # site for creating github auth service https://github.com/settings/developers
    'github': {
        'APP': {
            'client_id': '...',
            'secret': '...',
            'key': ''
        }
    }
}
MIDDLEWARE = [
    ...
    # REQUIRED by allauth
    'allauth.account.middleware.AccountMiddleware',
]
# =============================================================
```
Then in urls.py 
```python
...
path('accounts/', include('allauth.urls')),
...
```

Then in html
```html
{% load socialaccount %}

<a href="{% provider_login_url 'google' %}">Login with Google</a>
<a href="{% provider_login_url 'github' %}">Login with Github</a>
```

<br>
<br>

### Creating Google OAuth project
1. Go ahead and navigate to *https://console.cloud.google.com/* and click on APIs & Services. There you will find a dashboard and at the top click on the New Project button.
2. This will open another page and you will be prompted to enter a project name and location. Choose a name and organization and click on `create to proceed`.
3. Then the next step is to go back to the dashboard and click on Credentials>Create Credentials>OAuth Client ID as shown below.
   - (Please ensure that you are operating within the project that was recently created, which in our case is ‘DemoProject’.)
4. At the next page we will be asked to enter Application type, Name, Authorized JavaScript origins and Authorized redirect URIs. These information are important and should be added carefully as per the documentation.
   - Application Type = Web application
   - Name = DemoProject
   - Authorized JavaScript origins= *http://localhost:8000*
   - Authorized redirect URIs = *http://localhost:8000/accounts/google/login/callback/*

After that is done, lets go ahead and click on the create. This will then open a popup that provides us with our client_id and client secret so that we can copy and paste it in our `settings.py` file accordingly.

And then we can run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


<br><br><br>



#### 

# Permissions &&  Security 🔐 (advanced)   &&  📚 BeautifulSoup  
## Permissions
```python
class Product(models.Model): 
    # A custom permission called change_category has been defined.
    ...
    class Meta: 
        permissions = [('can_change_category', 'Can change category')] 
```
Here we can use decorators to check permissions every time before accessing any view
```python
@login_required  # is the first example of a decorator
@permission_required('products.can_change_category')  # is the second example of a decorator

# or we can use custom decorators
def testpermission(user): 
    if user.is_authenticated() and user.has_perm("myapp.change_category"): 
        return True 
    else: 
        return False 


from django.contrib.auth.decorators import user_passes_test 
@user_passes_test(testpermission)
def my_view(request): 
    ...
``` 

Similarly, the available permissions can be checked inside the template with perms.name syntax.  
For example:
```html
{% if perms.products.can_change_category %}
    <p>You can change category</p>
{% endif %}
```


# Signals   &&  Caching    &&   Sending Emails 📧 (advanced)


# 🌐 Internationalisation  &&  localisation  (advanced)


# Performance && optimization &&  Unit Tests
