FROM python:3.7-alpine

WORKDIR /app

COPY ./app.py /app
COPY ./calculator.py /app
COPY ./requirements.txt /app
ADD ./templates /app/templates

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./app.py"]
