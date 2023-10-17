from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserProfile(models.Model):

    gender_options = {

        ('male','MALE'),
        ('female','FEMALE')
    }

    zodiac_options = {

        ('aquarius','AQUARIUS'),
        ('pisces','PISCES'),
        ('aries','ARIES'),
        ('taurus','TAURUS'),
        ('gemini','GEMINI'),
        ('cancer','CANCER'),
        ('leo','LEO'),
        ('virgo','VIRGO'),
        ('libra','LIBRA'),
        ('scorpius','SCORPIUS'),
        ('sagittarius','SAGITTARIUS'),
        ('capricornus','CAPRICORNUS'),

    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField(upload_to='static/images/profile_pics/', blank=True, null=True)
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=6, choices=gender_options, default='None')
    country = models.CharField(max_length=255, blank=True)
    zodiac = models.CharField(max_length=15, choices=zodiac_options, default='None')

    def __str__(self):
        return self.user.username


class History(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.message
