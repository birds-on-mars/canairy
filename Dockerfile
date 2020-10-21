#!/bin/bash
FROM arm32v7/python:3.7

ENV DEBIAN_FRONTEND noninteractive

ARG AIRFLOW_HOME_USER=/usr/local/airflow
ENV AIRFLOW_HOME=$(AIRFLOW_HOME_USER)

USER root

RUN apt-get update -y
RUN apt-get install mpg123 -y

RUN pip3 install --upgrade pip
RUN pip3 install apache-airflow
RUN pip3 install mpg123

COPY . ${AIRFLOW_HOME_USER}

RUN chmod +x /usr/local/airflow/start_timer.sh

ENV AIRFLOW_HOME=${AIRFLOW_HOME_USER}

RUN airflow initdb

WORKDIR ${AIRFLOW_HOME_USER}

EXPOSE 8080

CMD ./start_timer.sh