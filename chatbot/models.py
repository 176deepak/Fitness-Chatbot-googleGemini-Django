from django.db import models

# Create your models here.

class UserImage(models.Model):
    image = models.ImageField(upload_to="userImage")
