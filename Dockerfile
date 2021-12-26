FROM python:3.10.1 as dependecies

COPY requirements.txt /requirements.txt
#COPY .env .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

FROM dependecies

COPY ./app /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

WORKDIR /app
