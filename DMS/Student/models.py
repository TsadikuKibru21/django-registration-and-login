from django.db import models

# Create your models here.


class Account(models.Model):
  email=models.EmailField(max_length=30)
  password=models.CharField(max_length=50)
  roleName=models.CharField(max_length=50)
  def __str__(self) -> str:
    return self.email
  acc=models.Manager()

    