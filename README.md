# Containerized Website

## The Stack
- Docker
- Nginx
- uWSGI
- Python
  - Flask
    - flask_wtf
    - SQLAlchemy
- HTML5
  - Bootstrap 4
- PostgreSQL

## Running the stack
``docker-compose up --build``

## Restarting Docker container
This maintains the rest of the containers of the stack running  
``docker-compose restart flask``

## Resources:  
- [Nginx, Flask, & Postgres multi-container setup with Docker Compose](http://www.ameyalokare.com/docker/2017/09/20/nginx-flask-postgres-docker-compose.html)  
- [Building a Flask app with Docker | Learning Flask](https://pythonise.com/series/learning-flask/building-a-flask-app-with-docker-compose)  
- [Dockerized Flask Implementation](https://github.com/Radu-Raicea/Dockerized-Flask)
- [Patterns for handling users (BCrypt & Login Manager)](https://exploreflask.com/en/latest/users.html)
- [Trello CSS](https://codepen.io/GeorgePark/pen/bLLzJK)
	- Did not want too spend too much time on the CSS, so I borrowed parts of this CSS sheet to prototype
