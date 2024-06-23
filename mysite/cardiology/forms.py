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
        fields = "__all__" 



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


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            model_field = self._meta.model._meta.get_field(field_name)
            if model_field.blank:
                field.required = False

        if 'patient_id' in self.fields:
            self.fields['patient_id'].queryset = Patient.objects.all()
            self.fields['patient_id'].label_from_instance = lambda obj: f"{obj.name} {obj.surname}"

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.doctor_id = self.user
        instance.time_date = timezone.now()
        if commit:
            instance.save()
        return instance


class ECGResultForm(BaseModelForm):
    class Meta:
        model = ECGResult
        exclude = ['doctor_id', 'time_date']


class LaboratoryAnalyteResultForm(BaseModelForm):
    class Meta:
        model = LaboratoryAnalyteResult
        exclude = ['doctor_id', 'time_date']


class PulseHeartBeatForm(BaseModelForm):
    class Meta:
        model = PulseHeartBeat
        exclude = ['doctor_id', 'time_date']


class BloodPressureForm(BaseModelForm):
    class Meta:
        model = BloodPressure
        exclude = ['doctor_id', 'time_date']


class RespirationForm(BaseModelForm):
    class Meta:
        model = Respiration
        exclude = ['doctor_id', 'time_date']


class BodyMassIndexForm(BaseModelForm):
    class Meta:
        model = BodyMassIndex
        exclude = ['doctor_id', 'time_date']


class PulseOximetryForm(BaseModelForm):
    class Meta:
        model = PulseOximetry
        exclude = ['doctor_id', 'time_date']


class ProblemDiagnosisForm(BaseModelForm):
    class Meta:
        model = ProblemDiagnosis
        exclude = ['doctor_id', 'time_date']


class MedicationManagementForm(BaseModelForm):
    class Meta:
        model = MedicationManagement
        exclude = ['doctor_id', 'time_date']