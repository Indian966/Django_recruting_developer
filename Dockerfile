FROM python:3

RUN apt-get update
RUN pip3 install django

WORKDIR /usr/src/app

COPY . .

WORKDIR ./django_test

CMD ["python3", "manage.py", "runserver", "0:8000"]

EXPOSE 8000