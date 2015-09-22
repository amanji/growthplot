# growthplot

This project uses Python's Django web framework on top of a PostgreSQL database. Ensure that you have Python and Postgres installed on your computer. You should be able to get all OS specific installation instructions for Python and Postgres by visitng the relevant websites.

##Installation instructions for Django 1.8:
To install Django you can use Python's package manager `pip`:
* If you're using MacOSX or Linux, in your terminal you can use the command `sudo pip install Django` to install the framework in your Python's installation directory.
* [This page](https://docs.djangoproject.com/en/1.8/topics/install/#installing-official-release) has more specifc installation instructions for your particular OS (for example if you're using Windows)
* You can check if Django successfully installed by entering `python -c "import django; print(django.get_version())"` in your terminal. You should see your currently installed version of Django at the prompt. If Django did not successfully install you will see a message like `“No module named django”`

##Hooking in Postgres
By default Django uses an SQLite database for backend storage. We've opted to use PostgreSQL since it is more robust and offers a vareity of useful features as the dataset grows. You will need to install the `Psycopg` adapter for Django to hook into a Postgres database.
* You can use `pip` to install the adapter using the the command `sudo pip install psycopg2` in your terminal.
* Consult [this page](http://initd.org/psycopg/docs/install.html) for your OS specific installation instructions.
* Actvate Postgres' interactive prompt by entering `psql` on your terminal as user `postgres`. Enter the following SQL commad: `CREATE DATABASE growthplot;`.

##Activate the app
* Enter the following commands in your terminal to set up the initial tables and initialize the framework:
`python manage.py migrate`
* To check that the app will run, activate a python server by entering `python manage.py runserver` in your terminal in the project root directory. Open up your browser and copy and paste the URL address (http://127.0.0.1:8000/
). You should see a page notifying you that the app works.

--------------------------------------------------

*** Liscencing Agreement ***

Unless otherwise explicitly specified, all works in this project are subject to the following liscence.

Copyright 2015 Growthplot

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
