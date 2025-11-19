from django.contrib.auth.models import User
from django.db import models
class UploadedFile(models.Model):
    file = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
