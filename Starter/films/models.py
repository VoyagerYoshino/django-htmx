from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Film(models.Model):
    name = models.CharField(max_length=128,unique=True)
    users = models.ManyToManyField(User,related_name="films")
    photo = models.ImageField(upload_to="film_photos",blank=True,null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

