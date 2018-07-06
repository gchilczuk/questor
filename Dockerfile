FROM python:3.6

RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt .
ADD ./manage.py .
RUN pip install -r requirements.txt