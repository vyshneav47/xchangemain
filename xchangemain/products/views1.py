from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from decimal import Decimal


@login_required
def up(request):
  if request.method == 'POST':
    # ... (product upload logic - handle form submission, image handling) ...
    product = Product.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        price= Decimal(request.POST['price']),
        image=request.FILES['image'],  # Access uploaded image
        owner=request.user
    )
    product.save()
    messages.success(request, 'Product uploaded successfully!')
    return redirect('product_list/')  # Redirect to product list after upload
  else:
    return render(request, 'product_upload.html')

def product_list(request):
  if request.user.is_authenticated:
    products = Product.objects.filter(owner=request.user)  # Filter by logged-in user
  else:
    products = None
  return render(request, 'product_list.html', {'products': products})

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request, username=username, password=password)
    if user is  None:
      login(request, user)
    #   messages.success(request, 'Login successful!')
      return redirect('up/')  # Redirect to product list after login
    else:
      return render(request,'error.html')
  return render(request, 'login.html')

