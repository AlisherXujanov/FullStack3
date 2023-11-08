
# Table of contents
1. [Introduction to APIs](#introduction-to-apis)
2. [API views](#api-views)
3. [Serialization and Deserialization](#serialization-and-deserialization)
4. [Authentication and Authorization](#authentication-and-authorization)
5. [JWT](#jwt)
6. [Filtering & Ordering & Pagination & Caching](#filtering--ordering--pagination--caching)

# Introduction to APIs 

### What is an API?
- API stands for Application Programming Interface. It is a set of rules that allow programs to talk to each other. The developer creates the API on the server and allows the client to talk to it.
- RU: API - это набор правил, которые позволяют программам общаться друг с другом. Разработчик создает API на сервере и позволяет клиенту общаться с ним.

### What is HTTP
- HTTP stands for Hypertext Transfer Protocol. It's a stateless, application-layer protocol for communicating between distributed systems, and is the foundation of the modern web.
- RU: HTTP - это протокол передачи гипертекста. Это безсостоятельный протокол прикладного уровня для обмена данными между распределенными системами и является основой современной веб-технологии.


### `TOPIC AGENDA`  
```markdown
1. HTTP Methods = [GET, POST, PUT, PATCH, DELETE]
2. HTTP requests  =  [ Version type, URL, Method, Headers, Body (optional) ]
3. HTTP response = [ Source, Length, Content-type, Headers, last-modified, status-code]
4. Naming conventions on Uniform Resource Identifier  and  Hierarchy and Params -?...=...
5. Essential tools for API development (Thunder-Client and Browser-Json-Formatter)
6. Creating a simple API using Django REST Framework
```


#### `HTTP Methods`  
```markdown
1. GET - Retrieve data from the server
2. POST - Submit data to the server
3. PUT - Update a resource
4. PATCH - Update part of a resource
5. DELETE - Delete a resource
```

#### `HTTP requests`  
```markdown
1. Version type - HTTP/1.1
2. URL - https://www.google.com
3. Method - GET
4. Headers - Accept: text/html
5. Body (optional) - { "name": "John" }
```

#### `HTTP response`  
```markdown
1. Source - https://www.google.com
2. Length - 12345
3. Content-type - text/html
4. Headers - Content-type: text/html
5. last-modified - 2020-01-01
6. status-code - 200
```

#### `Naming conventions on Uniform Resource Identifier  and  Hierarchy and Params -?...=...`  
```markdown
1. URI - Uniform Resource Identifier
2. URL - Uniform Resource Locator
3. Hierarchy - https://www.google.com/search?q=python
4. Params - ?q=python

EXAMPLE:
*`https://www.example.com/products/computers/laptops?brand=dell&price=500-1000`*
---------------------------------------------
- **https** is the scheme, which specifies the protocol used to access the resource (in this case, HTTPS).
- **www.example.com** is the domain name, which identifies the server that hosts the resource.
- **/products/computers/laptops** is the path, which specifies the location of the resource on the server.
- **?brand=dell&price=500-1000** is the query string, which contains additional parameters that can be used to filter or modify the resource.
```

#### `Essential tools for API development (Zunder-Client and Browser-Json-Formatter)`  
```markdown
1. Thunder-Client - https://www.thunderclient.com/
2. Browser-Json-Formatter - https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa
```


#### `Creating a simple API using Django REST Framework`  
https://www.django-rest-framework.org/tutorial/quickstart/



# API views

### Diffirent types of API-views
```python
from django.http import HttpResponse
from rest_framework import status

# For using a decorators
from rest_framework.response import Response
from rest_framework.decorators import api_view

# For using class-based views
from rest_framework.views import APIView
from rest_framework import generics, viewsets

@api_view(['GET', 'POST'])
def books_view(request):
    data = modal_to_dict(Book.objects.all())
    return Response({'message': 'Hello, world!'}, status=status.HTTP_200_OK)

class Books():
    @staticmethod
    @api_view(['GET', 'POST'])
    def books_view(request):
        return Response(
                        {'message': 'Hello, world!'}, 
                        status=status.HTTP_200_OK
                    )

# If we want to use it in the class-based view
class BookView(APIView):
	def get(self, request):
        all_books = Books.objects.all()
        books = BooksSerializer(all_books, many=True)
        return Response(books.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = BooksSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
```

### ViewSets
- ViewSets are simple class-based views, but they come with benefits. There are a few ViewSets classes available in DRF that you can use to quickly scaffold a functioning API CRUD project. You can also provide permission classes and throttle classes to allow authenticated API calls and rate limiting.
- RU: ViewSets - это простые представления на основе классов, но они имеют свои преимущества. В DRF доступно несколько классов ViewSets, которые вы можете использовать для быстрого создания функционирующего проекта API CRUD. Вы также можете предоставить классы разрешений и классы ограничения пропускной способности, чтобы разрешить аутентифицированные вызовы API и ограничение скорости.

Here are some of them that are mostly used:
1. **ViewSet** - does not provide any actions by default, and does not include the base set of generic view behavior.
So, you need to provide the implementation for each action explicitly.
2. **ModelViewSet** - provides CRUD functions with a single class. It accepts a queryset and a serializer class as required parameters. It also provides the following actions out of the box: list, retrieve, create, update, partial_update, destroy.
3. **ReadOnlyModelViewSet** - provides the read-only actions list and retrieve.

```python
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer

class MyViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = MyModel.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):  # POST
        pass

    def retrieve(self, request, pk=None):   # GET
        pass

    def update(self, request, pk=None):    # PUT
        pass

    def partial_update(self, request, pk=None):  # PATCH
        pass

    def destroy(self, request, pk=None):    # DELETE
        pass

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

```

### Generic views 
- Generic views are another way of quickly writing class-based views to scaffold fully functional CRUD API projects. There are several generic views that offer a particular functionality, like displaying resources or creating a new resource and so on. All you must do is extend these generic views to make your API endpoints work.
- RU: Обобщенные представления - это еще один способ быстрого написания представлений на основе классов для создания полностью функциональных проектов API CRUD. Существует несколько обобщенных представлений, которые предлагают определенную функциональность, например, отображение ресурсов или создание нового ресурса и т. Д. Все, что вам нужно сделать, это расширить эти обобщенные представления, чтобы ваши конечные точки API работали.

- CreateAPIView           - `POST` - Used for creating objects.
- ListAPIView             - `GET`  - Used for listing objects.
- RetrieveAPIView         - `GET`  - Display a single resource
- DestroyAPIView          - `DELETE` - Used for deleting objects.
- UpdateAPIView           - `PUT, PATCH` - Used for updating objects.
- ListCreateAPIView       - `GET, POST` - Used for listing and creating objects.
- RetrieveUpdateAPIView   - `GET, PUT, PATCH` - Used for retrieving and updating objects.
- RetrieveDestroyAPIView  - `GET, DELETE` - Used for retrieving and deleting objects.
- RetrieveUpdateDestroyAPIView - `GET, PUT, PATCH, DELETE` - Used for retrieving, updating, and deleting objects.

```python
from rest_framework import generics
from .models import MyModel

class MyCreateAPIView(generics.CreateAPIView):
    """ Used for creating objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class MyListAPIView(generics.ListAPIView):
    """ Used for listing objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

class MyRetrieveAPIView(generics.RetrieveAPIView):
    """ Used for retrieving a single object. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyDestroyAPIView(generics.DestroyAPIView):
    """ Used for deleting objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyUpdateAPIView(generics.UpdateAPIView):
    """ Used for updating objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyListCreateAPIView(generics.ListCreateAPIView):
    """ Used for listing and creating objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """ Used for retrieving and updating objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    """ Used for retrieving and deleting objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Used for retrieving, updating, and deleting objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

# =========================================================================
# in urls.py
...
path('api/.../', ...APIView.as_view(), name='...'),
...
```



### Permissions classes
- `AllowAny` - Allow any access
- `IsAuthenticated` - Allow access only to authenticated users
- `IsAdminUser` - Allow access only to admin users
- `IsAuthenticatedOrReadOnly` - Allow access to authenticated users (read-only) and allow access to non-authenticated users (read-only)


# Serialization and Deserialization

### Serializer
- In easy words, serializers are used to convert complex data, such as querysets and model instances, to native Python datatypes that can then be easily rendered into JSON, XML, or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
- RU: В простых словах сериализаторы используются для преобразования сложных данных, таких как наборы запросов и экземпляры моделей, в собственные типы данных Python, которые затем можно легко преобразовать в JSON, XML или другие типы контента. Сериализаторы также обеспечивают десериализацию, позволяя преобразовывать разобранные данные обратно в сложные типы после первичной проверки входных данных.


```python
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # NOTE: usually we don't want to add id field
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data:dict) -> Books:
        return Books.objects.create(**validated_data)

    def update(self, instance:Books, validated_data:dict) -> Books:
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
```

### ModelSerializer
- ModelSerializer is a shortcut to create a serializer class with fields that correspond to the Model fields. It will create a set of default fields for you, based on the model.
- RU: ModelSerializer - это сокращение для создания класса сериализатора с полями, соответствующими полям модели. Он создаст для вас набор полей по умолчанию на основе модели.

```python

```python
from rest_framework import serializers
DISCOUNT_IN_PERCENT = 10

class BookSerializer(serializers.ModelSerializer):
    price_in_discount = serializers.IntegerField(read_only=True, method_name='price_after_discount')
    author_name = serializers.CharField(read_only=True, method_name='current_user_as_author')

    # NOTE: 
    # 1. We can aslo use rename existing fields by using source attribute
    # ex: author_name = serializers.CharField(source='author.username')
    # 2. We can also use SerializerMethodField() to create a custom field
    # ex: price_in_discount = serializers.SerializerMethodField(method_name='price_after_discount')

    class Meta:
        model = Book
        fields = ['title', 'author_name', 'price_in_discount', 'description', 'created_at']

    def price_after_discount(self, obj:Book):
        discount_price = obj.price - (obj.price * DISCOUNT_IN_PERCENT / 100)
        return f'${discount_price} - ({DISCOUNT_IN_PERCENT}% discount)'

    def current_user_as_author(self, obj:Book):
        request = self.context.get('request')
        return request.user.username

# NOTE: To be able to get request object in serializer, 
#       you need to pass it in the view MySerializer(..., context={'request': request})

```


### Relationship serializer
- Let's say we have another model for 'genre' field of Books model.
- RU: Допустим, у нас есть другая модель для поля «жанр» модели Books.
```python
# models.py
class Genre(models.Model):
    slug = models.SlugField(unique=True) # this is for url
    name = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Books(models.Model):
    ...
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, default=1)
    ...
```

- So, we need to create a serializer for it and then use it in BooksSerializer
- RU: Итак, нам нужно создать для него сериализатор, а затем использовать его в BooksSerializer

```python
# serializers.py
class BooksSerializer(serializers.ModelSerializer):
    ...
    genre = serializers.HyperlinkedRelatedField(
        queryset=Genre.objects.all(),
        view_name='genre-detail',
        lookup_field='slug'
    )
    class Meta:
        model = Books
        fields = [..., 'genre', ...]
    ...
```

Then, we need to create a view for it.
```python
# NOTE: There is a convention you must follow when you create this view name. The rule is that you have to add -detail after the related field name, which is category in the MenuItemSerializer. This is why the view name was category-detail in this code. If the related field name was user, the view name would be user-detail. 
# RU: Существует соглашение, которого вы должны придерживаться при создании этого имени представления. Правило таково, что вы должны добавить -detail после имени связанного поля, которое является категорией в MenuItemSerializer. Вот почему имя представления было category-detail в этом коде. Если бы имя связанного поля было пользователь, имя представления было бы user-detail.

from .models import Genre 
from .serializers import GenreSerializer
from django.shortcuts import get_object_or_404 # for 404 error if the object does not exist
@api_view()
def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

# In urls.py
urlpatterns = [
    ...
    path('genres/<slug:slug>/', genre_detail, name='genre-detail'),
]
```


# Authentication and Authorization

### General information
- Authentication is the process of verifying the credentials of a user. Logging into websites with a username and password is a typical example of authentication. When the username and password match, the website recognizes the user and sets some cookies in the user’s browser. When the user visits another page on that website, the browser sends those cookies within the HTTP request header. The website recognizes the cookies as well as server-side session data and therefore doesn’t ask for credentials until the user logs out again.  
- RU: Аутентификация - это процесс проверки учетных данных пользователя. Вход на веб-сайты с именем пользователя и паролем - типичный пример аутентификации. Когда имя пользователя и пароль совпадают, веб-сайт распознает пользователя и устанавливает некоторые файлы cookie в браузере пользователя. Когда пользователь посещает другую страницу на этом веб-сайте, браузер отправляет эти файлы cookie в заголовке HTTP-запроса. Веб-сайт распознает файлы cookie, а также данные сеанса на стороне сервера и поэтому не запрашивает учетные данные до тех пор, пока пользователь снова не выйдет из системы.
- So, how does this work? Token-based authentication usually involves two steps in the API Architecture. First, the client identifies itself with a username and password. Then the API server gives it a bearer token. From there, the client includes the bearer token with every API call that it places. The API server verifies it and then allows the client to perform the action or not. This is where authorization comes in
- RU: Итак, как это работает? Аутентификация на основе токенов обычно включает два шага в архитектуре API. Сначала клиент идентифицирует себя с именем пользователя и паролем. Затем сервер API дает ему маркер-носитель. Оттуда клиент включает маркер-носитель в каждый вызов API, который он размещает. Сервер API проверяет его, а затем разрешает клиенту выполнять действие или нет. Вот тут и вступает авторизация.


- If the credentials are not valid, the client will receive a **`401 - Unauthorized`** HTTP status code.
- RU: Если учетные данные недействительны, клиент получит код состояния HTTP **`401 - Unauthorized`**.

- This is like coming to the office on the first day, submitting all your papers and documents, and then receiving your employee card. After that, only your employee card will be sufficient to get inside. Authentication works just like that!
- RU: Это похоже на то, как вы приходите в офис в первый день, сдаете все свои бумаги и документы, а затем получаете свою служебную карту. После этого только ваша служебная карта будет достаточна, чтобы попасть внутрь. Аутентификация работает так же!
  
- The two steps in the API authentication process can be represented by the following two diagrams.
- RU: Два шага в процессе аутентификации API можно представить следующими двумя диаграммами.

```markdown
1. Authentication      2. Authorization
+----------------+     +----------------+
|    Client      |     |     Client     |
|  +----------+  |     |  +----------+  |
|  |          |  |     |  |  Token   |  |
|  |  Login   |  |     |  |          |  |
|  |          |  |     |  |  Group   |  |
|  +----------+  |     |  +----------+  |
|  +----------+  |     |  +----------+  |
|  |          |  |     |  |          |  |
|  |  Token   |  |     |  |  Action  |  |
|  |          |  |     |  |          |  |
|  +----------+  |     |  +----------+  |
+----------------+     +----------------+
```

### Token based authentication

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken', # Allows us create a token for each user
    ...
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # Allows us to use token authentication throughout the project
        'rest_framework.authentication.TokenAuthentication',
    ],
}
if DEBUG:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += [
        'rest_framework.authentication.SessionAuthentication',
    ]
```

- For allowing token authentication, we need to create a token for each user. 
There, we would need obtain_auth_token
- RU: Для разрешения аутентификации токенов нам нужно создать токен для каждого пользователя.
  Там нам понадобится obtain_auth_token

```python
# urls.py
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    ...
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    ...
]
```

- Then, we need to create a view for it.
- RU: Затем нам нужно создать для этого представления.

```python
# views.py
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
    else:
        return Response({'error': 'Wrong credentials'}, status=400)
```

### Authorization
Authorization is the process of determining whether a user has access to a resource.
For example, if the user can delete or update something or not.
We can do this by adding certain user to a group and then check if the user is in that group or not. So, by doing this we authorize the user to do certain actions.
- RU: Авторизация - это процесс определения, имеет ли пользователь доступ к ресурсу.
  Например, может ли пользователь что-то удалить или обновить или нет.
  Мы можем сделать это, добавив определенного пользователя в группу, а затем проверив, находится ли пользователь в этой группе или нет. Таким образом, мы авторизуем пользователя на выполнение определенных действий.

```python
# views.py
@api_view()
def is_admin(request):
    if request.user.groups.filter(name='admin').exists():
        return Response({'message': 'You are admin'}, status=200)
    else:
        return Response({'message': 'You are not admin'}, status=400)
```

### Throttling
- Throttling means that we can postpone the request for a certain amount of time.
For example, we can allow only 5 requests per minute.
We need this to prevent the server from overloading.
Sometimes, a user can try to break in by trying to guess the password. So, we can prevent this by adding throttling. This way, that user will be able to make only 5 requests per minute.
- RU: Throttling означает, что мы можем отложить запрос на определенное время.
  Например, мы можем разрешить только 5 запросов в минуту.
  Нам нужно это, чтобы предотвратить перегрузку сервера.
  Иногда пользователь может попытаться взломать, пытаясь угадать пароль. Таким образом, мы можем предотвратить это, добавив ограничение. Таким образом, этот пользователь сможет делать только 5 запросов в минуту.

```python
# settings.py

REST_FRAMEWORK = {
    ...
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle', # for anonymous users
        'rest_framework.throttling.UserRateThrottle', # for authenticated users
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/minute', # 3 requests per minute
        'user': '5/minute', # 5 requests per minute
    }
}
```
Then we need to add it to the view.
```python
# views.py
from rest_framework.throttling import UserRateThrottle

class MyView(APIView):
    throttle_classes = [UserRateThrottle]
    ...
```

If we want to create manual throttling for a specific view, we can do it like this:
```python
# views.py
from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'

class MyView(APIView):
    throttle_classes = [TenCallsPerMinute]
    ...

# settings.py
...
DEFAULT_THROTTLE_RATES = {
    ...
    'ten': '10/minute',
    ...
}
```


### Djoser
- Djoser is a REST implementation of Django authentication system. It provides a set of endpoints for authentication, registration, password reset, etc.
- RU: Djoser - это реализация REST системы аутентификации Django. Он предоставляет набор конечных точек для аутентификации, регистрации, сброса пароля и т. Д.

`pipenv || pip   install djoser`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'djoser', # It is vital to add it after rest_framework
    # RU: Важно добавить его после rest_framework
    ...
]

DJOSER = {
    "USER_ID_FIELD": "username", # We use username for login
    # "LOGIN_FIELD": "email", # We can use email or username for login
    # "USER_CREATE_PASSWORD_RETYPE": True, # We can use this to make user retype the password
}

# urls.py
urlpatterns = [
    ...
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    ...
    # handy endpoints list
    # --------------------------------
    # /auth/users/ - list of all users
    # /auth/users/me/ - current user
    # /auth/users/confirm/ - confirm email
    # /auth/users/resend_activation/ - resend activation email
    # /auth/users/set_password/ - set new password
    # /auth/users/reset_password/ - reset password
    # /auth/users/reset_password_confirm/ - confirm reset password
    # /auth/token/login/ - login
    # /auth/token/logout/ - logout
]

```



# JWT
### JWT Authentication
- JSON Web Token (JWT) is  a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. (Digitally signed means that it is signed using a secret key that only the server knows.)
- RU: JSON Web Token (JWT) - это компактный и автономный способ безопасной передачи информации между сторонами в виде объекта JSON. Эту информацию можно проверить и доверять, потому что она цифровая подпись. (Цифровая подпись означает, что она подписана с использованием секретного ключа, который знает только сервер.)

`pipenv || pip   install djangorestframework_simplejwt`

[JWT-documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html?highlight=settings)

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    ...
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # TokenAuthentication is replaced with JWTAuthentication
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    ...
}

# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    ...
    path('api/token/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ...
]

# settings.py
# JWT settings
from datetime import timedelta
REFRESH_TOKEN_LIFETIME_SIX_WEEKS = 42 # days

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=REFRESH_TOKEN_LIFETIME_SIX_WEEKS),
    'ROTATE_REFRESH_TOKENS': True, # If True, refresh tokens will be rotated
    # That means that after each request we will get a new refresh token
    # RU: Если True, токены обновления будут поворачиваться
    # Это означает, что после каждого запроса мы получим новый токен обновления
    'AUTH_HEADER_TYPES': ('Bearer',),
    # In the client we need to send the token in the header like this:
    # Authorization: bearer <token>
}
```
`NOTE`
- access token expires and is not valid after settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
But, this does NOT mean that client has to login again. Client can use refresh token to get a new access token. 
- RU: токен доступа истекает и не действителен после settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
  Но это НЕ означает, что клиенту нужно снова войти в систему. Клиент может использовать токен обновления, чтобы получить новый токен доступа.  

---
---

If we want to some extra validation in the token, we can do it like this:
```python
# views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer

# serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class MyTokenRefreshSerializer(TokenRefreshSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

# urls.py
urlpatterns = [
    ...
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```








# Filtering  &  Ordering  &  Pagination  &  Caching

### Filtering
[This is the link that we can visit filtering](https://www.django-rest-framework.org/api-guide/filtering/)

By filtering we can filter the data that we want to get. 
For example, we can filter the books by author or by title.


So, if the user asks books by author, we can do it like this:
ex: `http://domain-name.com/api/books/?author=John`

```python
# views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author=author)
        return queryset

# ===========================================
# -- OR -- in our case
# ===========================================
class BookList(APIView): 
    def get(self, request):
        author = request.query_params.get('author')
        if author:
            books = Book.objects.filter(author=author)
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# urls.py
urlpatterns = [
    ...
    path('api/books/', BookList.as_view(), name='book-list'),
    ...
]
```

### Ordering
[This is the link that we can visit for ordering](https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter)

By ordering we can order the data that we want to get.
For example, we can order the books by title or by author.

```python
# views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset

# ===========================================
# -- OR -- in our case
# ===========================================
class BookList(APIView): 
    def get(self, request):
        ordering = request.query_params.get('ordering')
        if ordering:
            books = Book.objects.order_by(ordering)
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
```

### Pagination
[This is the link that we can visit for pagination](https://www.django-rest-framework.org/api-guide/pagination/)
By pagination we can limit the number of objects that we want to get.
For example, we can limit the number of books that we want to get.

```python
# settings.py
REST_FRAMEWORK = {
    ...
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 1,
    ...
}


# views.py
from rest_framework import generics
class BookList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# ===========================================
# -- OR -- in our case
# ===========================================
from rest_framework.pagination import PageNumberPagination
class BookList(APIView): 
    def get(self, request):
        books = Book.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
```


### Caching 

```python
SECOND = 1
MINUTE = SECOND * 60
HOUR = MINUTE * 60

SHORT_WAIT = SECOND * 3
LONG_WAIT = MINUTE * 10

SHORT_CACHING_TIME = MINUTE * 30
LONG_CACHING_TIME = HOUR * 2
```

By caching we can improve the performance of our API.
When we visit first time the api it loads normally but
when we visit it again it loads faster because it is cached.

```python
@method_decorator(cache_page(LONG_CACHING_TIME)) 
# cache_page => This means that we cache the page for a certain amount of time
# By default, it caches the page for 15 minutes
# RU: Это означает, что мы кэшируем страницу на определенное время
# По умолчанию он кэширует страницу на 15 минут

@method_decorator(vary_on_headers("Authorization",))
# vary_on_headers => We need this because we want to cache the page for each user separately
# By default, it caches the page for all users together
# RU: Нам это нужно, потому что мы хотим кэшировать страницу для каждого пользователя отдельно
# По умолчанию он кэширует страницу для всех пользователей вместе
```

[This is the link that we can visit for filtering](https://www.django-rest-framework.org/api-guide/caching/)





