#!/usr/bin/env bash

# Install requirements if they exist
if [ -e "/opt/airflow/requirements.txt" ]; then
    $(command python) pip install --user -r /opt/airflow/requirements.txt
fi

# Initialize the database
if [ ! -f "/opt/airflow/airflow.db" ]; then
    airflow db init &&
    airflow users create \
        --username admin \
        --firstname admin \
        --lastname admin \
        --role Admin \
        --email admin@example.com \
        --password admin
fi

# Execute the command passed to the script
exec airflow "$@"
