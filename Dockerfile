FROM tiangolo/uwsgi-nginx:python3.6

ADD ./uwsgi.ini .
ADD ./requirements.txt .
RUN pip install -r requirements.txt