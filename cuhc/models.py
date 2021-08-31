from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)

def __str__(self):
        return self.full_name

class article (models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    images=models.ImageField(upload_to='')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
