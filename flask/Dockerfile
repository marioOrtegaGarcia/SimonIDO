# Pulling python image
FROM python:3.7.2-stretch

# Merging Dockerfiles
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/flask/src
COPY requirements.txt /opt/services/flask/src/
WORKDIR /opt/services/flask/src

# Installing dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#COPY . /opt/services/flask/src
EXPOSE 8080

# Running uWSGI
CMD ["uwsgi", "app.ini"]

