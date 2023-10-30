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
	def get(self, request, pk):
    	return Response(
                      {"message":"single book with id " + str(pk)},
                       status.HTTP_200_OK
                   )
	def put(self, request, pk):
    	return Response(
                       {"title":request.data.get('title')}, 
                       status.HTTP_200_OK
                    )

```

### ViewSets
ViewSets are simple class-based views, but they come with benefits. There are a few ViewSets classes available in DRF that you can use to quickly scaffold a functioning API CRUD project. You can also provide permission classes and throttle classes to allow authenticated API calls and rate limiting.

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
Generic views are another way of quickly writing class-based views to scaffold fully functional CRUD API projects. There are several generic views that offer a particular functionality, like displaying resources or creating a new resource and so on. All you must do is extend these generic views to make your API endpoints work.

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
        serializer.save(user=self.request.user)

class MyListAPIView(generics.ListAPIView):
    """ Used for listing objects. """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

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
- `DjangoModelPermissions` - Allow access only to authenticated users with the correct permission (read-only)


# Serializers

# Authentication and Authorization

### Authentication
Authentication is the process of verifying the credentials of a user. Logging into websites with a username and password is a typical example of authentication. When the username and password match, the website recognizes the user and sets some cookies in the user’s browser. When the user visits another page on that website, the browser sends those cookies within the HTTP request header. The website recognizes the cookies as well as server-side session data and therefore doesn’t ask for credentials until the user logs out again.  
So, how does this work? Token-based authentication usually involves two steps in the API Architecture. First, the client identifies itself with a username and password. Then the API server gives it a bearer token. From there, the client includes the bearer token with every API call that it places. The API server verifies it and then allows the client to perform the action or not. This is where authorization comes in

If the credentials are not valid, the client will receive a **`401 - Unauthorized`** HTTP status code.

This is like coming to the office on the first day, submitting all your papers and documents, and then receiving your employee card. After that, only your employee card will be sufficient to get inside. Authentication works just like that!

The two steps in the API authentication process can be represented by the following two diagrams.

```markdown
1. Authentication      2. Authorization
+----------------+     +----------------+
|    Client      |     |     Client     |
|  +----------+  |     |  +----------+  |
|  |          |  |     |  |          |  |
|  |  Login   |  |     |  |  Token   |  |
|  |          |  |     |  |          |  |
|  +----------+  |     |  +----------+  |
|  +----------+  |     |  +----------+  |
|  |          |  |     |  |          |  |
|  |  Token   |  |     |  |  Action  |  |
|  |          |  |     |  |          |  |
|  +----------+  |     |  +----------+  |
+----------------+     +----------------+
```
### Authorization





# Relationships and Hyperlinks

# Requests and Responses

# Throttling  &  Filtering  &  Pagination

