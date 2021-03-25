from django.db import models
from django.contrib.auth import get_user_model


User  = get_user_model()


class Icecream(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()
    rating = models.IntegerField()
    avatar = models.ImageField(blank=True, null=True)







