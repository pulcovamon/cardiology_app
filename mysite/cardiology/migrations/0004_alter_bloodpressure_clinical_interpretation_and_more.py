# Generated by Django 4.2.11 on 2024-05-21 05:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cardiology", "0003_alter_doctor_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloodpressure",
            name="clinical_interpretation",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="bloodpressure",
            name="comment",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="bloodpressure",
            name="diastolic",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="bloodpressure",
            name="mean_arterial_pressure",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="bloodpressure",
            name="systolic",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="bloodpressure",
            name="time_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="bodymassindex",
            name="bmi",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name="bodymassindex",
            name="clinical_interpretation",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="bodymassindex",
            name="comment",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="bodymassindex",
            name="time_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="arterial_heart_rate",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="comment",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="conclusion",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="ecg_diagnosis",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="ecg_type",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="p_amplitude",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="p_axis",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="p_duration",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="pr_interval_global",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="q_amplitude",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="q_duration",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="qrs_axis",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="qrs_duration_global",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="qt_interval_global",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="qtc_interval_global",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="r_amplitude",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="r_duration",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="rr_interval_global",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="s_amplitude",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="s_duration",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="t_axis",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="time_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="ecgresult",
            name="ventricular_heart_rate",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="laboratoryanalyteresult",
            name="analyte_name",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name="laboratoryanalyteresult",
            name="analyte_result",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name="laboratoryanalyteresult",
            name="analyte_result_sequence",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="laboratoryanalyteresult",
            name="time_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="medicationmanagement",
            name="amount",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="medicationmanagement",
            name="clinical_indication",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="medicationmanagement",
            name="comment",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="medicationmanagement",
            name="double_checked",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="medicationmanagement",
            name="time_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="patient",
            name="city",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name="patient",
            name="email",
            field=models.CharField(
                blank=True,
                max_length=25,
                validators=[django.core.validators.EmailValidator()],
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="nationality",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="patient",
            name="postal_code",
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name="patient",
            name="street",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name="patient",
            name="zip_code",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="problemdiagnosis",
            name="comment",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="problemdiagnosis",
            name="diagnosis_certeinity",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="problemdiagnosis",
            name="severity",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="problemdiagnosis",
            name="time_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="problemdiagnosis",
            name="variant",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="pulseheartbeat",
            name="character",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="pulseheartbeat",
            name="clinical_description",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="pulseheartbeat",
            name="comment",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="pulseheartbeat",
            name="irregular_type",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="pulseheartbeat",
            name="irregularity",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="pulseheartbeat",
            name="presence",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="pulseheartbeat",
            name="rate",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="pulseheartbeat",
            name="time_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="pulseoximetry",
            name="clinical_interpretation",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="pulseoximetry",
            name="comment",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="pulseoximetry",
            name="spco",
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name="pulseoximetry",
            name="spmet",
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name="pulseoximetry",
            name="spo2",
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name="pulseoximetry",
            name="spoc",
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name="pulseoximetry",
            name="time_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="respiration",
            name="clinical_interpretation",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="respiration",
            name="comment",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="respiration",
            name="presence",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="respiration",
            name="rate",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="respiration",
            name="regularity",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="respiration",
            name="time_date",
            field=models.DateField(blank=True),
        ),
    ]
