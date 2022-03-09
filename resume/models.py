from django.db import models

# Create your models here.
class Resume(models.Model):
    resume  = models.FileField( upload_to="resume", max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)