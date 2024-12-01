# Django + Docker + Rabbitmq + celery + gunicorn + Postgresql + Nginx

I create my petproject opened in Docker

My app have:

 -Search
 
 -Authenticate
 
 -Registrate
 
 -Create order
 
 -Cart for product

## Tech stack

### Back-end

- Django
- Postgresql
- Celery
- Rabbitmq
- Nginx

## Notable opinions and extensions

Django is an opinionated framework and I've added a few extra opinions based on having Dockerized and deployed a number of Django projects.

- **Packages and extensions**:
    - *[gunicorn](https://gunicorn.org/)* for an app server in both development and production


- **Linting and formatting**:
    - *[flake8](https://github.com/PyCQA/flake8)* is used to lint the code base


- **Django apps**:
    - Added `account` app that's responsible for your personal data
    - Added `cart` app that's responsible for your storing your purchases
    - Added `orders` app that's responsible for your orders
    - Added `shop` app that's responsible for explore and choice products

- **Frameworks**:
  
    -Rabbitmq as broker
  
    -Celery as worker for background tasks
  
    -Django as base our project
  
    -Postgresql as our database 

    -Nginx as HTTP web server

## Running this app

You'll need to have [Docker installed](https://docs.docker.com/get-docker/).
It's available on Windows, macOS and most distros of Linux.

Install 7Zip pac or use command of git install on your PC:
```sh
git clone https://github.com/ShadowDubina/Django-Shop.git
```
Next:

```sh
cd Django-Shop
cd config

```

#### Build everything:

The first time you run this it's going to take 5-10 minutes depending on your internet connection speed and computer's hardware specs. That's because it's going to download a few Docker images and build the Python

```sh
docker compose up --build
```

#### Check it out in a browser:

Visit <http://localhost:1337/shop> in your favorite browser.


#### If you want create admin and add data:
You need open 2 cmd

Then:
```sh
cd Django-Shop
cd config
```
You need open docker, open container, see container id, copy, and paste it in place to this command:
```sh
docker exec -t -i container_id bash
```
Further you need:
```sh
python manage.py createsuperuser
```
and fill in the form:

-username:admin

-email:

-password:admin

-password again:admin

-create:y

#### COMPLETE!

