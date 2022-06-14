# About Mozio Transport Suppliers

Mozio Transport Suppliers is a web app that enables transport suppliers to define custom polygons as their \"service area\" to simplify the process of capturing zip codes, cities etc

---

## Installation and Usage

1. First you need to clone this repository from [github](https://github.com/Njokosi/mozio_transport_suppliers).
   
2. Head over to the cloned repository.
   
3. Activate your virtual enviroment and install dependencies. 
   - If you're using [python poetry](https://python-poetry.org/docs/cli/) run `poetry install`
   - If you're using pip to install dependencies run `pip install -r requirements.txt`.
  
4. Create .env file from the project root, View the sample .env.example on how to add parameters.
   - For any other database configuration url please refer [dj_database_url](https://github.com/kennethreitz/dj-database-url)
   
5. Run `python manage.py migrate` to migrate the database migrations.
   
6. Run `python manage.py runserver` to start server.
   
7. Head over to http://localhost:8000/documentation to see the documentation on how to integrate the API using frontend architecture of your preference.

---


## VIRTUAL ENVIRONMENT
Mozio Transport Suppliers is powered with [poetry](https://python-poetry.org/) to configure it's dependencies. Follow [instructions](https://python-poetry.org/docs/) on how to install on your machine.


:wink: Enjoy the service

---