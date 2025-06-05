#framework 

A [[MVT]] framework written in [[Python]]

Supports [[SQL]] and [[JavaScript]]. Also includes the [[DTL]]

<hr>
## Links

[Django - First App](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

https://docs.djangoproject.com/en/4.2/ref/forms/fields/

[Sjango tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)


<hr>
## Notes
- Django HTML has access to request e.g. {{ request.user }}
- Every project should contain 1 or more apps.

<hr>
## Create a new project

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
pip install djangorestframework

django-admin startproject drinks .

=> Will need to add 'drinks' to INSTALLED_APPS in settings.py
```

```python
python manage.py runserver
http://127.0.0.1:8000/
```

## Create a new App

``python manage.py startapp portfolio

index.html
---









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

