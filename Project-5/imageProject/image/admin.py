from django.contrib import admin

# Register your models here.
from .models import Image
admin.site.register(Image)

from .models import UserData
admin.site.register(UserData)