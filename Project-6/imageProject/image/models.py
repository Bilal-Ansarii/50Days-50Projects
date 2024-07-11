from django.db import models

# Create your models here.
class Image(models.Model):
   #caption=models.CharField(max_length=100)
   image=models.ImageField(upload_to="img/%y")
   is_profile_picture = models.BooleanField(default=False)
   def __str__(self):
      return self.caption
   
class UserData(models.Model):
   uname=models.CharField(max_length=50)
   def __str__(self):
      return self.uname