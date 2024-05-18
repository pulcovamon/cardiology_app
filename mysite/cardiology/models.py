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
    nationality = models.CharField(max_length=10)
    city = models.CharField(max_length=15)
    street = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    postal_code = models.CharField(max_length=5)
    email = models.CharField(max_length=25, validators=[EmailValidator()])


class ECGResult(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    ecg_type = models.CharField(max_length=25)
    arterial_heart_rate = models.IntegerField()
    ventricular_heart_rate = models.IntegerField()
    qt_interval_global = models.IntegerField()
    qtc_interval_global = models.IntegerField()
    pr_interval_global = models.IntegerField()
    qrs_duration_global = models.IntegerField()
    rr_interval_global = models.IntegerField()
    p_axis = models.CharField(max_length=15)
    qrs_axis = models.CharField(max_length=15)
    t_axis = models.CharField(max_length=15)
    p_amplitude = models.IntegerField()
    p_duration = models.IntegerField()
    q_amplitude = models.IntegerField()
    q_duration = models.IntegerField()
    r_amplitude = models.IntegerField()
    r_duration = models.IntegerField()
    s_amplitude = models.IntegerField()
    s_duration = models.IntegerField()
    conclusion = models.CharField(max_length=50)
    ecg_diagnosis = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    time_date = models.DateField()


class LaboratoryAnalyteResult(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    analyte_result_sequence = models.IntegerField()
    analyte_name = models.CharField(max_length=25)
    analyte_result = models.CharField(max_length=25)
    time_date = models.DateField(blank=False)


class PulseHeartBeat(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    presence = models.BooleanField()
    rate = models.IntegerField()
    irregularity = models.BooleanField()
    irregular_type = models.BooleanField()
    character = models.CharField(max_length=50)
    clinical_description = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    time_date = models.DateField(blank=False)


class BloodPressure(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    mean_arterial_pressure = models.IntegerField()
    clinical_interpretation = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    time_date = models.DateField(blank=False)


class Respiration(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    presence = models.BooleanField()
    rate = models.IntegerField()
    regularity = models.BooleanField()
    clinical_interpretation = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    time_date = models.DateField(blank=False)


class BodyMassIndex(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    bmi = models.DecimalField(decimal_places=2, max_digits=4)
    clinical_interpretation = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    time_date = models.DateField(blank=False)


class PulseOximetry(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    spo2 = models.DecimalField(decimal_places=1, max_digits=4)
    spoc = models.DecimalField(decimal_places=1, max_digits=4)
    spco = models.DecimalField(decimal_places=1, max_digits=4)
    spmet = models.DecimalField(decimal_places=1, max_digits=4)
    clinical_interpretation = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    time_date = models.DateField(blank=False)


class ProblemDiagnosis(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    diagnosis_name = models.CharField(max_length=50, blank=False)
    variant = models.CharField(max_length=50)
    severity = models.IntegerField() # enum
    diagnosis_certeinity = models.IntegerField() # enum
    stop_date = models.DateField(blank=False, default=None)
    comment = models.CharField(max_length=250)
    time_date = models.DateField(blank=False)


class MedicationManagement(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False)
    medication_item = models.CharField(max_length=50, blank=False)
    clinical_indication = models.CharField(max_length=50)
    double_checked = models.BooleanField()
    amount = models.IntegerField()
    stop_date = models.DateField(blank=False, default=None)
    comment = models.CharField(max_length=250)
    time_date = models.DateField(blank=False)

