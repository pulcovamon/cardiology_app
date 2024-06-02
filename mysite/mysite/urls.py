"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from cardiology.views import (
    IndexView,
    PatientListView,
    PatientDetailView,
    PatientRecordsView,
    PatientCreateView,
    DoctorCreateView,
    ECGResultFormView,
    LaboratoryAnalyteResultFormView,
    PulseHeartBeatFormView,
    BloodPressureFormView,
    RespirationFormView,
    BodyMassIndexFormView,
    PulseOximetryFormView,
    ProblemDiagnosisFormView,
    MedicationManagementFormView,
    ECGResultDetailView,
    LaboratoryAnalyteResultDetailView,
    PulseHeartBeatDetailView,
    BloodPressureDetailView,
    RespirationDetailView,
    BodyMassIndexDetailView,
    PulseOximetryDetailView,
    ProblemDiagnosisDetailView,
    MedicationManagementDetailView,
    DoctorDetailView,
    success_view,
    DoctorListView,
    generate_json
)


urlpatterns = [
    path('', IndexView.as_view(redirect_authenticated_user=True), name='index'),
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patients/<int:pk>/records/', PatientRecordsView.as_view(), name='patient_records'),
    path('ecg-result/', ECGResultFormView.as_view(), name='ecg_result_form'),
    path('laboratory-analyte-result/', LaboratoryAnalyteResultFormView.as_view(), name='laboratory_analyte_result_form'),
    path('pulse-heartbeat/', PulseHeartBeatFormView.as_view(), name='pulse_heartbeat_form'),
    path('blood-pressure/', BloodPressureFormView.as_view(), name='blood_pressure_form'),
    path('respiration/', RespirationFormView.as_view(), name='respiration_form'),
    path('body-mass-index/', BodyMassIndexFormView.as_view(), name='body_mass_index_form'),
    path('pulse-oximetry/', PulseOximetryFormView.as_view(), name='pulse_oximetry_form'),
    path('problem-diagnosis/', ProblemDiagnosisFormView.as_view(), name='problem_diagnosis_form'),
    path('medication-management/', MedicationManagementFormView.as_view(), name='medication_management_form'),
    path('ecg-result/<int:pk>/', ECGResultDetailView.as_view(), name='ecg_result_detail'),
    path('laboratory-analyte-result/<int:pk>/', LaboratoryAnalyteResultDetailView.as_view(), name='laboratory_analyte_result_detail'),
    path('pulse-heartbeat/<int:pk>/', PulseHeartBeatDetailView.as_view(), name='pulse_heartbeat_detail'),
    path('blood-pressure/<int:pk>/', BloodPressureDetailView.as_view(), name='blood_pressure_detail'),
    path('respiration/<int:pk>/', RespirationDetailView.as_view(), name='respiration_detail'),
    path('body-mass-index/<int:pk>/', BodyMassIndexDetailView.as_view(), name='body_mass_index_detail'),
    path('pulse-oximetry/<int:pk>/', PulseOximetryDetailView.as_view(), name='pulse_oximetry_detail'),
    path('problem-diagnosis/<int:pk>/', ProblemDiagnosisDetailView.as_view(), name='problem_diagnosis_detail'),
    path('medication-management/<int:pk>/', MedicationManagementDetailView.as_view(), name='medication_management_detail'),
    path('patients/create', PatientCreateView.as_view(), name='create_patient'),
    path('doctors/create/', DoctorCreateView.as_view(), name='create_doctor'),
    path('doctors/account/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctors', DoctorListView.as_view(), name='doctor_list'),
    path('success/', success_view, name='success_url'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('<str:model_name>/<int:pk>/generate-json/', generate_json, name='generate_json'),]

