from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render

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
    template_name = 'cardiology/doctor_list.html'  # Název šablony pro zobrazení seznamu lékařů
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
    success_url = "patients/"
    template_name = (
        "cardiology/form.html"  # Použití společné šablony pro vytvoření
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Patient"  # Název stránky pro vytvoření pacienta
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


class ECGResultFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = ECGResultForm
    success_url = "/success/"
    extra_context = {"form_title": "ECG result"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LaboratoryAnalyteResultFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = LaboratoryAnalyteResultForm
    success_url = "/success/"
    extra_context = {"form_title": "Laboratory Analyte result"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PulseHeartBeatFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = PulseHeartBeatForm
    success_url = "/success/"
    extra_context = {"form_title": "Pulse heartbeat"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BloodPressureFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = BloodPressureForm
    success_url = "/success/"
    extra_context = {"form_title": "Blood pressure"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RespirationFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = RespirationForm
    success_url = "/success/"
    extra_context = {"form_title": "Respiration"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BodyMassIndexFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = BodyMassIndexForm
    success_url = "/success/"
    extra_context = {"form_title": "BMI"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PulseOximetryFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = PulseOximetryForm
    success_url = "/success/"
    extra_context = {"form_title": "Pulse oximetry"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProblemDiagnosisFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = ProblemDiagnosisForm
    success_url = "/success/"
    extra_context = {"form_title": "Problem/diagnosis"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MedicationManagementFormView(FormView):
    template_name = "cardiology/form.html"
    form_class = MedicationManagementForm
    success_url = "/success/"
    extra_context = {"form_title": "Medication"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RecordDetailView(DetailView):
    template_name = "cardiology/record.html"
    context_object_name = "record"


class ECGResultDetailView(RecordDetailView):
    model = ECGResult

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = "ECG result detail"
        return context


class LaboratoryAnalyteResultDetailView(RecordDetailView):
    model = LaboratoryAnalyteResult

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = "Laboratory analyte result detail"
        return context


class PulseHeartBeatDetailView(RecordDetailView):
    model = PulseHeartBeat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = "Pulse heartbeat detail"
        return context


class BloodPressureDetailView(RecordDetailView):
    model = BloodPressure

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = "Blood pressure detail"
        return context


class RespirationDetailView(RecordDetailView):
    model = Respiration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = "Respiration detail"
        return context


class BodyMassIndexDetailView(RecordDetailView):
    model = BodyMassIndex

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = "BMI detail"
        return context


class PulseOximetryDetailView(RecordDetailView):
    model = PulseOximetry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = "Pulse oximetry detail"
        return context


class ProblemDiagnosisDetailView(RecordDetailView):
    model = ProblemDiagnosis

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = "Problem/diagnosis detail"
        return context


class MedicationManagementDetailView(RecordDetailView):
    model = MedicationManagement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["record_title"] = " Medication detail"
        return context