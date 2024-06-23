from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import F
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
from django.apps import apps

from .forms import (
    DoctorForm,
    PatientForm,
    DoctorLoginForm,
    ECGResultForm,
    LaboratoryAnalyteResultForm,
    PulseHeartBeatForm,
    BloodPressureForm,
    RespirationForm,
    BodyMassIndexForm,
    PulseOximetryForm,
    ProblemDiagnosisForm,
    MedicationManagementForm,
)
from .models import (
    Patient,
    Doctor,
    ECGResult,
    LaboratoryAnalyteResult,
    PulseHeartBeat,
    BloodPressure,
    Respiration,
    BodyMassIndex,
    PulseOximetry,
    ProblemDiagnosis,
    MedicationManagement,
)


def success_view(request):
    return render(request, 'cardiology/success.html')


class IndexView(LoginView):
    authentication_form = DoctorLoginForm
    template_name = "cardiology/index.html"
    redirect_url = reverse_lazy('doctor_detail')


class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctor
    template_name = 'cardiology/doctor_detail.html'
    context_object_name = 'doctor'

    def get_object(self):
        username = self.request.user.username
        return get_object_or_404(Doctor, username=username)


class DoctorListView(ListView):
    model = Doctor
    template_name = 'cardiology/doctor_list.html'
    context_object_name = 'doctors'


class PatientListView(ListView):
    model = Patient
    template_name = "cardiology/patient_list.html"
    context_object_name = "patients"


class PatientDetailView(DetailView):
    model = Patient
    template_name = "cardiology/patient.html"
    context_object_name = "patient_records"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = self.get_object()
        current_medications = MedicationManagement.objects.filter(
            patient_id=patient.id, stop_date=None
        )
        current_diagnoses = ProblemDiagnosis.objects.filter(
            patient_id=patient.id, stop_date=None
        )
        context["current_medications"] = current_medications
        context["current_diagnoses"] = current_diagnoses
        context["patient"] = patient
        return context


class PatientRecordsView(ListView):
    model = Patient
    template_name = "cardiology/patient_records.html"
    context_object_name = "patient_records"

    def get_queryset(self):
        patient_id = self.kwargs["pk"]
        patient = Patient.objects.get(pk=patient_id)
        ecg_results = ECGResult.objects.filter(patient_id=patient_id)
        laboratory_results = LaboratoryAnalyteResult.objects.filter(
            patient_id=patient_id
        )
        pulse_heartbeats = PulseHeartBeat.objects.filter(patient_id=patient_id)
        blood_pressures = BloodPressure.objects.filter(patient_id=patient_id)
        respirations = Respiration.objects.filter(patient_id=patient_id)
        bmis = BodyMassIndex.objects.filter(patient_id=patient_id)
        pulse_oximetries = PulseOximetry.objects.filter(patient_id=patient_id)
        problem_diagnoses = ProblemDiagnosis.objects.filter(patient_id=patient_id)
        medication_managements = MedicationManagement.objects.filter(
            patient_id=patient_id
        )
        return {
            "patient": patient,
            "ecg_results": ecg_results,
            "laboratory_results": laboratory_results,
            "pulse_heartbeats": pulse_heartbeats,
            "blood_pressures": blood_pressures,
            "respirations": respirations,
            "bmis": bmis,
            "pulse_oximetries": pulse_oximetries,
            "problem_diagnoses": problem_diagnoses,
            "medication_managements": medication_managements,
        }


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('patient_list')
    template_name = (
        "cardiology/form.html"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Patient"
        return context


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = "cardiology/form.html"
    success_url = reverse_lazy('success_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Add Doctor"
        return context


class BaseFormView(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('success_url')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ECGResultFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = ECGResultForm
    extra_context = {"form_title": "ECG result"}

class LaboratoryAnalyteResultFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = LaboratoryAnalyteResultForm
    extra_context = {"form_title": "Laboratory Analyte result"}

class PulseHeartBeatFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = PulseHeartBeatForm
    extra_context = {"form_title": "Pulse heartbeat"}

class BloodPressureFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = BloodPressureForm
    extra_context = {"form_title": "Blood pressure"}

class RespirationFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = RespirationForm
    extra_context = {"form_title": "Respiration"}

class BodyMassIndexFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = BodyMassIndexForm
    extra_context = {"form_title": "BMI"}

class PulseOximetryFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = PulseOximetryForm
    extra_context = {"form_title": "Pulse oximetry"}

class ProblemDiagnosisFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = ProblemDiagnosisForm
    extra_context = {"form_title": "Problem/diagnosis"}

class MedicationManagementFormView(BaseFormView):
    template_name = "cardiology/form.html"
    form_class = MedicationManagementForm
    extra_context = {"form_title": "Medication"}


class RecordDetailView(DetailView):
    template_name = "cardiology/record.html"
    context_object_name = "examination"


class ECGResultDetailView(RecordDetailView):
    model = ECGResult

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "ECG result detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


class LaboratoryAnalyteResultDetailView(RecordDetailView):
    model = LaboratoryAnalyteResult

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "Laboratory analyte result detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


class PulseHeartBeatDetailView(RecordDetailView):
    model = PulseHeartBeat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "Pulse heartbeat detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


class BloodPressureDetailView(RecordDetailView):
    model = BloodPressure

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "Blood pressure detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


class RespirationDetailView(RecordDetailView):
    model = Respiration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "Respiration detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


class BodyMassIndexDetailView(RecordDetailView):
    model = BodyMassIndex

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "BMI detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


class PulseOximetryDetailView(RecordDetailView):
    model = PulseOximetry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "Pulse oximetry detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


class ProblemDiagnosisDetailView(RecordDetailView):
    model = ProblemDiagnosis

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "Problem/diagnosis detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


class MedicationManagementDetailView(RecordDetailView):
    model = MedicationManagement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examination_title"] = "Medication detail"
        context["title"] = self.model._meta.model_name
        patient = context["examination"].patient_id
        context["patient"] = f"{patient.name} {patient.surname}"
        context["fields"] = [(field.verbose_name, getattr(self.object, field.name)) for field in self.model._meta.fields if field.name not in ['id', 'title', 'patient_id', 'datetime', 'comment']]
        return context


def export_to_fhir(request, model_name, pk):
    model = apps.get_model('cardiology', model_name)
    examination = get_object_or_404(model, id=pk)
    fhir_observation = generate_fhir_observation(examination)
    return JsonResponse(fhir_observation)


def generate_fhir_observation(examination):
    fhir_observation = {
        "resourceType": "Observation",
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "exam",
                "display": "Examination"
            }]
        }],
        "subject": {
            "reference": f"Patient/{examination.patient_id.id}",
            "display": f"{examination.patient_id.name} {examination.patient_id.surname}"
        },
        "effectiveDateTime": examination.time_date.isoformat() if examination.time_date else ""
    }
    
    if isinstance(examination, ECGResult):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": examination.ecg_type
            }]
        }
        fhir_observation["component"] = [
            {
                "code": {
                    "coding": [{
                        "system": "http://loinc.org",
                        "code": "",
                        "display": "Arterial Heart Rate"
                    }]
                },
                "valueInteger": examination.arterial_heart_rate
            },
            {
                "code": {
                    "coding": [{
                        "system": "http://loinc.org",
                        "code": "",
                        "display": "Ventricular Heart Rate"
                    }]
                },
                "valueInteger": examination.ventricular_heart_rate
            },
            {
                "code": {
                    "coding": [{
                        "system": "http://loinc.org",
                        "code": "",
                        "display": "QT interval"
                    }]
                },
                "valueInteger": examination.qt_interval_global
            },
            {
                "code": {
                    "coding": [{
                        "system": "http://loinc.org",
                        "code": "",
                        "display": "QRS complex"
                    }]
                },
                "valueInteger": examination.qrs_duration_global
            }
        ]
    elif isinstance(examination, LaboratoryAnalyteResult):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": examination.analyte_name
            }]
        }
        fhir_observation["valueString"] = examination.analyte_result if examination.analyte_result else ""
    elif isinstance(examination, PulseHeartBeat):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": "Heart rate"
            }]
        }
        fhir_observation["valueQuantity"] = {
            "value": examination.rate,
            "unit": "beats/minute",
            "system": "http://unitsofmeasure.org",
            "code": "/min"
        }
    elif isinstance(examination, BloodPressure):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": "Blood pressure systolic & diastolic"
            }]
        }
        fhir_observation["component"] = [
            {
                "code": {
                    "coding": [{
                        "system": "http://loinc.org",
                        "code": "8480-6",
                        "display": "Systolic blood pressure"
                    }]
                },
                "valueQuantity": {
                    "value": examination.systolic,
                    "unit": "mmHg",
                    "system": "http://unitsofmeasure.org",
                    "code": "mm[Hg]"
                }
            },
            {
                "code": {
                    "coding": [{
                        "system": "http://loinc.org",
                        "code": "8462-4",
                        "display": "Diastolic blood pressure"
                    }]
                },
                "valueQuantity": {
                    "value": examination.diastolic,
                    "unit": "mmHg",
                    "system": "http://unitsofmeasure.org",
                    "code": "mm[Hg]"
                }
            }
        ]
    elif isinstance(examination, Respiration):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": "Respiratory rate"
            }]
        }
        fhir_observation["valueQuantity"] = {
            "value": examination.rate,
            "unit": "breaths/minute",
            "system": "http://unitsofmeasure.org",
            "code": "/min"
        }
    elif isinstance(examination, BodyMassIndex):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": "Body mass index (BMI) [Ratio]"
            }]
        }
        fhir_observation["valueQuantity"] = {
            "value": examination.bmi,
            "unit": "kg/m2",
            "system": "http://unitsofmeasure.org",
            "code": "kg/m2"
        }
    elif isinstance(examination, PulseOximetry):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": "Oxygen saturation in Arterial blood by Pulse oximetry"
            }]
        }
        fhir_observation["valueQuantity"] = {
            "value": examination.spo2,
            "unit": "%",
            "system": "http://unitsofmeasure.org",
            "code": "%"
        }
    elif isinstance(examination, ProblemDiagnosis):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": "Diagnosis"
            }]
        }
        fhir_observation["valueString"] = examination.diagnosis_name
    elif isinstance(examination, MedicationManagement):
        fhir_observation["code"] = {
            "coding": [{
                "system": "http://loinc.org",
                "code": "",
                "display": "Medication management"
            }]
        }
        fhir_observation["valueString"] = examination.medication

    return fhir_observation