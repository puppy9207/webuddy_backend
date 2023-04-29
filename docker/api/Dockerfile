# FROM cnstark/pytorch:1.12.1-py3.9.12-cuda11.6.2-ubuntu20.04
FROM python:3.10-slim-buster

# set working directory
RUN mkdir -p app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive


# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# opencv
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx libglib2.0-0

# install python dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip \
  && pip install -r requirements.txt


# add app
COPY . .