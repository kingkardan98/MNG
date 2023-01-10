# MNNG - Manage you money

MNNG (read Manage) is a simple Python project that showcases backend programming capabilities of the author.

It simulates a money manager, in a simple but elegant way: a user can create multiple "members", which represent the different monetary accounts the user possesses.

The website is fully written in Python, and it uses a lightweight SQLite3 database.
Resource routing, HTTP responses and database operations are all managed using the <a href='https://www.djangoproject.com'>Django framework.</a>
Basic HTML is used to render the website, with some CSS and JavaScript styling.

Now hosted on <a href='http://frbambina.eu.pythonanywhere.com/'>PythonAnywhere.</a>

Still extremely proud of the project's size and attention to detail.

### Now fully bilingual! 🇮🇹🇬🇧

---
---

# How to deploy the website locally?

Simple! Navigate to <mark style='background-color: gray;'>MNG/settings.py</mark> and follow the instructions given by the code, as shown below:

```python

# SECURITY WARNING: keep the secret key used in production secret!

# Comment this section out for local deployment
SECRET_KEY = os.getenv("SECRET_KEY")

# Uncomment this section for local deployment
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
# Turn this into True for local deployment.
DEBUG = False

```

At this point, in your root directory, run two commands:

```
- python3 manage.py makemigrations
- python3 manage.py migrate
```

This initializes the database.

Finally, create a super user using the command

```
python3 manage.py createsuperuse
```
The prompt itself will guide you. With this account, you will be able to access your local admin page, and manage the database hands-on from there.

All set!