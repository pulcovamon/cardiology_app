from django.core.validators import RegexValidator, EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class DoctorManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)

        # Set a default password if none is provided
        if password is None:
            password = ""

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class Doctor(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    email = models.EmailField(max_length=255, validators=[EmailValidator()], blank=False, unique=True)
    specialist = models.CharField(max_length=25, blank=False)
    username = models.CharField(max_length=25, blank=False, unique=True, default=email)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = DoctorManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'surname']

    def __str__(self):
        return f'{self.name} {self.surname}'


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    birth_certificate_number = models.CharField(max_length=10, validators=[RegexValidator(regex=r"\d{2}(0[1-9]|1[0-2]|5[1-9]|6[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])\/?\d{3,4}")], blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    nationality = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    street = models.CharField(max_length=15, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    postal_code = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(max_length=25, validators=[EmailValidator()], blank=True, null=True)


class ECGResult(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    ecg_type = models.CharField(max_length=25, blank=True, null=True)
    arterial_heart_rate = models.IntegerField(blank=True, null=True)
    ventricular_heart_rate = models.IntegerField(blank=True, null=True)
    qt_interval_global = models.FloatField(blank=True, null=True)
    qtc_interval_global = models.FloatField(blank=True, null=True)
    pr_interval_global = models.FloatField(blank=True, null=True)
    qrs_duration_global = models.FloatField(blank=True, null=True)
    rr_interval_global = models.FloatField(blank=True, null=True)
    p_axis = models.CharField(max_length=15, blank=True, null=True)
    qrs_axis = models.CharField(max_length=15, blank=True, null=True)
    t_axis = models.CharField(max_length=15, blank=True, null=True)
    p_amplitude = models.FloatField(blank=True, null=True)
    p_duration = models.FloatField(blank=True, null=True)
    q_amplitude = models.FloatField(blank=True, null=True)
    q_duration = models.FloatField(blank=True, null=True)
    r_amplitude = models.FloatField(blank=True, null=True)
    r_duration = models.FloatField(blank=True, null=True)
    s_amplitude = models.FloatField(blank=True, null=True)
    s_duration = models.FloatField(blank=True, null=True)
    conclusion = models.CharField(max_length=50, blank=True, null=True)
    ecg_diagnosis = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)


class LaboratoryAnalyteResult(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    analyte_result_sequence = models.IntegerField(blank=True, null=True)
    analyte_name = models.CharField(max_length=25, blank=True, null=True)
    analyte_result = models.CharField(max_length=25, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)


class PulseHeartBeat(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    presence = models.BooleanField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    irregularity = models.BooleanField(blank=True, null=True)
    irregular_type = models.BooleanField(blank=True, null=True)
    character = models.CharField(max_length=50, blank=True, null=True)
    clinical_description = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)


class BloodPressure(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    systolic = models.IntegerField(blank=True, null=True)
    diastolic = models.IntegerField(blank=True, null=True)
    mean_arterial_pressure = models.IntegerField(blank=True, null=True)
    clinical_interpretation = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)


class Respiration(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    presence = models.BooleanField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    regularity = models.BooleanField(blank=True, null=True)
    clinical_interpretation = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)


class BodyMassIndex(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    bmi = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    clinical_interpretation = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)


class PulseOximetry(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    spo2 = models.DecimalField(decimal_places=1, max_digits=4, blank=True, null=True)
    spoc = models.DecimalField(decimal_places=1, max_digits=4, blank=True, null=True)
    spco = models.DecimalField(decimal_places=1, max_digits=4, blank=True, null=True)
    spmet = models.DecimalField(decimal_places=1, max_digits=4, blank=True, null=True)
    clinical_interpretation = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)


class ProblemDiagnosis(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    diagnosis_name = models.CharField(max_length=50, blank=False)
    variant = models.CharField(max_length=50, blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)  # enum
    diagnosis_certeinity = models.IntegerField(blank=True, null=True)  # enum
    stop_date = models.DateField(blank=True, default=None, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)


class MedicationManagement(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    medication_item = models.CharField(max_length=50, blank=False)
    clinical_indication = models.CharField(max_length=50, blank=True, null=True)
    double_checked = models.BooleanField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    stop_date = models.DateField(blank=True, default=None, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    time_date = models.DateField(blank=True, null=True)
