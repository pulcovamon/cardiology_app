# Generated by Django 4.2.11 on 2024-05-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cardiology", "0004_alter_bloodpressure_clinical_interpretation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicationmanagement",
            name="stop_date",
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name="problemdiagnosis",
            name="stop_date",
            field=models.DateField(blank=True, default=None),
        ),
    ]