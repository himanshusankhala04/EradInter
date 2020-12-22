
from django.db import models

# Create your models here. datetime.strptime(date_str, "%d-%m-%Y").date()

class personalInfo(models.Model):
    #u_id = models.CharField(max_length=50)
    first_name = models.CharField(default="",max_length=50)
    middle_name = models.CharField(default="",max_length=50)
    last_name = models.CharField(default="",max_length=50)
    email = models.CharField(default="",max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(default="NA",max_length=10)

    country = models.CharField(default="",max_length=30)
    state = models.CharField(default="",max_length=30)
    city = models.CharField(default="",max_length=30)
    address_line1 = models.CharField(default="",max_length=200)
    address_line2 = models.CharField(default="",max_length=200)
    pincode = models.CharField(default="",max_length=10)
    primary_contact = models.CharField(default="",max_length=20)
    secondary_contact = models.CharField(default="",max_length=20)

    primary_speciality = models.CharField(default="",max_length=30)
    secondary_speciality = models.CharField(default="",max_length=30)
    Expirience_in_Years = models.CharField(default="",max_length=10)
    NPI_or_GMC_or_IMC_number = models.CharField(default="",max_length=10)
    profile_image = models.FileField(upload_to='images/', default="")

    medical_school = models.CharField(default="",max_length=50)
    Residency_or_Specialist_Training_or_PG = models.CharField(default="",max_length=50)
    Fellowship = models.CharField(default="",max_length=50)
    board_certification = models.CharField(default="",max_length=50)
    states_to_practice = models.CharField(default="",max_length=50)
    Revalidation_or_Continuing_Medical_Education_Year = models.CharField(default="",max_length=50)
    Honors_or_Awards_or_Recognition = models.CharField(default="",max_length=50)
    publication = models.CharField(default="",max_length=50)
    Hospital_Privileges_to_practice = models.CharField(default="",max_length=50)
    Resume_or_CV = models.FileField(upload_to='images/', default="")
    Description = models.CharField(default="",max_length=400)
    Comments = models.CharField(default="",max_length=400)
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"