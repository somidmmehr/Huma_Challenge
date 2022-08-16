FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /service_1
COPY requirements.txt /service_1/requirements.txt
RUN pip install -r requirements.txt
COPY . /service_1

CMD python manage.py runserver 0.0.0.0:8000