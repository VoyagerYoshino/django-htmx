from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Film(models.Model):
    name = models.CharField(max_length=128)
    users =models.ManyToManyField(User,related_name='films')
    
    def __str__(self):
        return self.name
    
class UserFilm(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    film = models.ForeignKey(Film,on_delete=models.CASCADE)
    order = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.film.name + " " + str(self.pk)
    
    class Meta:
        ordering = ['order']
    
