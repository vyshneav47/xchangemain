from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from .models import Customer  

def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    
    if Customer.objects.filter(username=username).exists():
      
      return render(request, 'register.html', {'error': 'Username already exists'})
    if Customer.objects.filter(email=email).exists():
      
      return render(request, 'register.html', {'error': 'Email already exists'})

   
    customer = Customer(username=username, email=email, password=password)
    customer.save()

  
    return redirect('login/')  

  return render(request, 'register.html')



def logout_view(request):
  logout(request)

  return render(request,'login.html') 


