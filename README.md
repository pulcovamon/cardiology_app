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
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd mysite
python manage.py makemigrations cardiology
python manage.py migrate
python manage.py runserver  
```
