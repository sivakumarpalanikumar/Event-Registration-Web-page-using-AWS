from django.db import models

# Create your models here.
class formcontact(models.Model):
    name = models.CharField(max_length=25)
    rollno = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    part = models.CharField(max_length=300)
    dept = models.CharField(max_length=25)
    year = models.CharField(max_length=25)
    sect = models.CharField(max_length=25)
    paperpresentation = models.BooleanField(null=True)
    projectpresentation = models.BooleanField(null=True)
    quiz = models.BooleanField(null=True)
    coding = models.BooleanField(null=True)
    nontechnical = models.BooleanField(null=True)


