from django.shortcuts import render, redirect
from .form import ImageForm, UserDataForm
from .models import Image, UserData

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        userdetail_form = UserDataForm(request.POST, request.FILES)
        
        if form.is_valid() and userdetail_form.is_valid():
            image = form.cleaned_data['image']
            uname = userdetail_form.cleaned_data['uname']  # Get the username from the form
            
            # Check if there's an existing profile picture for the user
            existing_profile_picture = Image.objects.filter(is_profile_picture=True).first()
            
            if existing_profile_picture:
                # If there's an existing profile picture, update it
                existing_profile_picture.image = image
                existing_profile_picture.save()
            else:
                # If there's no existing profile picture, create a new one
                form.instance.is_profile_picture = True
                form.save()
                
            obj = form.instance
            # Save the user data along with the username
            user_data = userdetail_form.save(commit=False)
            user_data.uname = uname
            user_data.save()
            print(uname)
            return render(request, "index.html", {"obj": obj, "uname": uname})  # Pass the username to the template
    else:
        form = ImageForm()  
        userdetail_form = UserDataForm()

    img = Image.objects.filter(is_profile_picture=True).first()
    return render(request, "index.html", {"img": img, "form": form, "userdetail_form": userdetail_form})
