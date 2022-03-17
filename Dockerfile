FROM python:3.8.4

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

RUN pip isntall -r requirements.txt

COPY . /app

EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi