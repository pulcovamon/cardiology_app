from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.utils import timezone

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


class DoctorLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')

    class Meta:
        fields = ['username', 'password']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"  # nebo specifikujte pole, která chcete zobrazit ve formuláři



class DoctorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Doctor
        fields = ['name', 'surname', 'phone_number', 'email', 'specialist', 'username', 'password']

    def save(self, commit=True):
        doctor = super().save(commit=False)
        doctor.password = make_password(self.cleaned_data['password'])
        if commit:
            doctor.save()
        return doctor


class ECGResultForm(forms.ModelForm):
    class Meta:
        model = ECGResult
        exclude = ['doctor_id', 'time_date']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.doctor_id = self.user
        instance.time_date = timezone.now()
        if commit:
            instance.save()
        return instance


class LaboratoryAnalyteResultForm(forms.ModelForm):
    class Meta:
        model = LaboratoryAnalyteResult
        fields = "__all__"


class PulseHeartBeatForm(forms.ModelForm):
    class Meta:
        model = PulseHeartBeat
        fields = "__all__"


class BloodPressureForm(forms.ModelForm):
    class Meta:
        model = BloodPressure
        fields = "__all__"


class RespirationForm(forms.ModelForm):
    class Meta:
        model = Respiration
        fields = "__all__"


class BodyMassIndexForm(forms.ModelForm):
    class Meta:
        model = BodyMassIndex
        fields = "__all__"


class PulseOximetryForm(forms.ModelForm):
    class Meta:
        model = PulseOximetry
        fields = "__all__"


class ProblemDiagnosisForm(forms.ModelForm):
    class Meta:
        model = ProblemDiagnosis
        fields = "__all__"


class MedicationManagementForm(forms.ModelForm):
    class Meta:
        model = MedicationManagement
        fields = "__all__"
