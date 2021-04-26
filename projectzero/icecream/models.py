from django.db import models
from django.contrib.auth import get_user_model


User  = get_user_model()


class Icecream(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='имя',
        help_text='название мороженого'
    )
    desc = models.TextField(
        verbose_name='описание',
        help_text='описание мороженого'
    )
    price = models.IntegerField(
        verbose_name='цена',
        help_text='цена мороженого'
    )
    rating = models.IntegerField(
        verbose_name='рейтинг',
        help_text='рейтинг мороженого'
    )
    avatar = models.ImageField(
        blank=True, 
        null=True,
        verbose_name='картинка',
        help_text='картинка мороженого'
    )