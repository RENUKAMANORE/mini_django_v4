from django.db import models
from django.utils import timezone

# Create your models here.
from django.contrib.auth .models import User

class Portal(models.Model):
    name = models.CharField(max_length=250,unique=True)
    description = models.CharField(max_length=250)

    def launch(self):
        self.save()

    def __str__(self):
        return self.name

class Title(models.Model):
    roll_no = models.CharField(max_length=250)
    last_updated = models.DateTimeField(default=timezone.now())
    portal = models.ForeignKey(Portal, on_delete=Portal)

class JobDescription(models.Model):
    rol = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.rol

class Applicant(models.Model):
    job_description = models.ForeignKey(
        JobDescription , on_delete=models.CASCADE)
    cover_letter = models.CharField(max_length=250)

    def __str__(self):
        return self.job_description


