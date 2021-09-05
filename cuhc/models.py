from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)

class article (models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    pdf=models.FileField(upload_to='pdf/')

class images (models.Model):
    id_image=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.full_name
    def __str__(self):
        return self.title
    def __str__(self):
        return self.id_image