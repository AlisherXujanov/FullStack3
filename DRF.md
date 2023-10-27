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