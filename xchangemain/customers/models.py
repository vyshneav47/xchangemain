from django.db import models

class Customer(models.Model):
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(unique=True)  # Assuming emails are unique for simplicity
  password = models.CharField(max_length=100)  # This is BAD for production (store hashed passwords)

  def __str__(self):
    return self.username


# Create your models here.
