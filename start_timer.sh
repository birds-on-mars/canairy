#!/bin/bash

set -m

airflow scheduler &
airflow webserver
