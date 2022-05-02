from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume  = models.FileField(upload_to="resume", max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    types =  models.CharField(max_length=10, default='pdf')

    def __str__(self):
        return self.user.first_name


class ScanHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    score = models.FloatField()
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
    