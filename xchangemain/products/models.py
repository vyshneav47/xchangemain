from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model

class Product(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='products/', blank=True)  # Optional image field
  owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Link product to a User

  def __str__(self):
    return self.title
# Create your models here.
