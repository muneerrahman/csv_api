# CSV Upload API

## Overview
This Django REST Framework API allows uploading a CSV file containing user data. 
It validates the data and saves valid records to the database.

## Requirements
asgiref==3.9.1
Django==5.2.6
djangorestframework==3.16.1
sqlparse==0.5.3
tzdata==2025.2

## Installation
Clone the repository:
git clone https://github.com/muneerrahman/csv_api.git
cd csv_api

Install requirements:
pip install -r requirement.txt

## Running the Server
python manage.py migrate
python manage.py runserver

## Using the API
- URL: `http://127.0.0.1:8000/api/users/upload-csv/`
- Method: `POST`
- Body: Form-data → Key: `file` → Value: sample_input.csv
- Response: JSON containing saved_records, rejected_records, errors


You can also find full sample files in the `samples/` folder:
- [sample_input.csv](sample_input.csv)
- [sample_output.json](sample_output.JSON)

<img width="1917" height="974" alt="api_csv" src="https://github.com/user-attachments/assets/2d07ec2a-6bbd-407e-b6a7-32e3b21a32a5" />
