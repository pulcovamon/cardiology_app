# Simple Information system for cardiology clinic
## Semestral project for school subject ELD

## Features
- **Doctors**:
    - Create new doctor accounts
    - Login as doctor with username and password
    - List of doctors with name and contact information
- **Patients**:
    - Create new patients
    - List of all patients
    - Detail of each patient with basic info about current medication and diagnosis
    - Create new record about examination, medication prescription or diagnosis
    - List of patients records (from examination, medication or diagnosis) with date
    - Detail of each record with possibility to export into FHIR in json format
- **Examinations**>
    - ECG
    - Laboratory analysis
    - Pulse heartbeat
    - Blood pressure
    - Respiration
    - BMI
    - Pulse oximetry
 
Start app:
```
poetry install
cd mysite
poetry run python manage.py makemigrations cardiology
poetry run python manage.py migrate
poetry run python manage.py runserver  
```
