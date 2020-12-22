# Generated by Django 3.1.3 on 2020-12-21 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201221_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinfo',
            old_name='Honors_Awards_Recognition',
            new_name='Honors_or_Awards_or_Recognition',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='NPI_GMC_IMC_number',
            new_name='NPI_or_GMC_or_IMC_number',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='Residency_SpecialistTraining_PG',
            new_name='Residency_or_Specialist_Training_or_PG',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='Resume_CV',
            new_name='Resume_or_CV',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='Revalidation_ContinuingMedicalEducationYear',
            new_name='Revalidation_or_Continuing_Medical_Education_Year',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='add_line1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='add_line2',
            new_name='address_line2',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='e_mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='first_n',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='last_n',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='middle_n',
            new_name='middle_name',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='pin_code',
            new_name='pincode',
        ),
    ]
