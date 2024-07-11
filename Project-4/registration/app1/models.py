from django.db import models

# Create your models here.
class user_details(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    user_name = models.SlugField(max_length=30, unique=True)
    email_id = models.EmailField()
    profile_picture = models.ImageField(null=True, blank=True)