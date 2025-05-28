from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    ROLE_CHOICES = [
        ('staff', 'Staff'),
        ('non staff', 'Non staff'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
