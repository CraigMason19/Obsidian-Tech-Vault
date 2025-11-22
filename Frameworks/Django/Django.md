#framework 

A [[MVT]] framework written in [[Python]]

Supports [[SQL]] and [[JavaScript]]. Also includes the [[DTL]]

<hr>
## Links

[Django - First App](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

https://docs.djangoproject.com/en/4.2/ref/forms/fields/

[Sjango tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)

[Package to allow CSS modification](https://github.com/adamchainz/django-browser-reload)

<hr>

## TOC

- [[#Create a new project]]
- [[#Create a new App]]
- [[#Environment Variables & Secrets]]


## Notes
- Django HTML has access to request e.g. {{ request.user }}
- Every project should contain 1 or more apps.

<hr>
### Create a new project

```
example: drinks (can't use hyphen for names e.g. minimal-portfolio -> minimal_portfolio)
.venv the is virtual environment's name
. means current directory



cd desktop // Or other location
mkdir drinks
cd drinks
python -m venv .venv

=> open folder in VS Code. Save workspace. Open workspace terminal
.venv/scripts/activate

pip install django 

django-admin startproject drinks .

=> Will need to add 'drinks' to INSTALLED_APPS in settings.py
```

```python
python manage.py runserver
http://127.0.0.1:8000/ # Django default
```

### Create a new App

``python manage.py startapp example_app

then in example_app.views.py
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

example_app.urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

Project level urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('whatever/', include('example_app.urls')), 
]
```

add app to installed apps in `settings.py`

```python
INSTALLED_APPS = [
	...
    'foobar',
    'whatever_app',
]
```

---
### Create a HTML page with CSS

Make sure static is enabled in settings.py
```python
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    # ... your apps
]
```

Create a HTML file `example_app/templates/index.html`
```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Polls Index</title>
    <link rel="stylesheet" href="{% static 'polls/style.css' %}">
</head>
<body>
    <h1>Hello, world. You're at the polls index.</h1>
    <p>This is a styled page using Django templates.</p>
</body>
</html>
```

create a static folder `example_app/static` and add a CSS file

replace the contents of example_app/views.py to

```python
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
```





you can have multiple django apps in a django project

Django apps that are purely functional modules with no URLs of their own. These are often called service apps, utility apps, or domain logic apps, and they’re a great way to isolate reusable logic without exposing routes.
 
 index.html
 
---
## Environment Variables & Secrets


- Install `dotenv` 
	- `pip install python-dotenv`
	
- Update your `settings.py`:
```python
import os
from dotenv import load_dotenv
 
# Loads .env in dev, does nothing in prod
load_dotenv()  
 
REQUIRED_ENV_VARS = [
    "DJANGO_SECRET_KEY",
]

for var in REQUIRED_ENV_VARS:
    if not os.getenv(var):
        raise ValueError(f"{var} is not set in the environment!")

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
```

- Create `.env` file in project root (next to manage.py)
	- **MAKE SURE TO ADD TO GITIGNORE!!!!!!!!!**

- It can then be used like this
```python
from django.conf import settings

settings.SECRET_KEY
```

---
## Messages

https://docs.djangoproject.com/en/5.2/ref/contrib/messages

My music theory docs bake app has an example of this, also styling akin to bootstrap alerts





## Commands

new project
In the terminal
```Python
django-admin startproject airline
cd airline
code .

python manage.py startapp flights

python manage.py runserver
http://127.0.0.1:8000/
```
#### Superuser
If you create a superuser it allows you to go to /admin, sign in and manipulate the DB data directly.
You will also need to add the models you want to manipulate to (app)/admin.py
```Python
python manage.py createsuperuser


# admin.py
from django.contrib import admin

from .models import Email

# Register your models here.
admin.site.register(Email)
```

## Migration

A 2step-process
1 - create a migration (changes to DB structure)
2 - Take those instructions and change them in the DB

```Python
python manage.py makemigrations
python manage.py migrate
```

---

```python
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```








<hr>
## get() vs filter()[0] vs first()

All slightly different ways of doing a similar thing. I preferer the first() paradigm.
#### [`get()`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") 
If you know there is only one object that matches your query, you can use the [`get()`] method to return the object directly.
e.g. ```one_entry = Entry.objects.get(pk=1)```

- If there are no results that match the query, [`get()`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") will raise a [`Model.DoesNotExist`](https://docs.djangoproject.com/en/4.2/ref/models/class/#django.db.models.Model.DoesNotExist)` exception.
- If more than object was found, it raises a [`Model.MultipleObjectsReturned`](https://docs.djangoproject.com/en/4.2/ref/models/class/#django.db.models.Model.MultipleObjectsReturned "django.db.models.Model.MultipleObjectsReturned") exception:
#### [`filter()`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") 
Will always give you a [`QuerySet`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), even if only a single object matches the query - in this case, it will be a [`QuerySet`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing a single element.
To get the first element you can call `filter()[0]`.
#### first
Will return `None` if no object was found. So will not throw an exception.

<hr>

