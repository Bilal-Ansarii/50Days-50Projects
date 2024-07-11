from django import forms
from .models import Image, UserData

class ImageForm(forms.ModelForm):
   class Meta:
      model = Image
      fields = ['image']

class UserDataForm(forms.ModelForm):
   uname=forms.TextInput()
   class Meta:
      model = UserData
      fields = ['uname']      