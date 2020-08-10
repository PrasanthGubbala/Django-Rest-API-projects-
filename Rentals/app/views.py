from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render,redirect

from app.models import ProviderDetails


def main(request):
    return render(request, 'main/main.html')

def provider_login(request):
    return render(request, 'main/provider_login.html')

def provider_login_check(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        provider = ProviderDetails.objects.get(email=email)
        if email == provider.email and password == provider.password:
            return render(request,'provider/provider_home.html')
        elif email != provider.email:
            messages.error(request,'Invalid Username')
            return redirect('provider_login')
        elif password != provider.password:
            messages.error(request,"Password did'nt match")
            return redirect('provider_login')
        else:
            messages.error(request,'Invalid Username/Password')
            return redirect('provider_login')


    except ProviderDetails.DoesNotExist as de:
        messages.error(request,de)
        return redirect('provider_login')


def provider_registration(request):
    return render(request,'main/provider_registration.html')

def provider_registration_save(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    gender = request.POST.get('gender')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    photo = request.FILES['photo']
    
    print(photo)
    if password == password2:
        try:
            ProviderDetails(first_name=fname,last_name=lname,gender=gender,contact=contact,address=address,email=email,password=password,photo=photo).save()
            messages.success(request,'Registered Successfully')
            return redirect('provider_login')
        except IntegrityError as ie:
            messages.error(request,'User detail are already exist')
            return redirect('provider_registration')

    else:
        messages.error(request,"Password did'nt match")
        return redirect('provider_registration')

