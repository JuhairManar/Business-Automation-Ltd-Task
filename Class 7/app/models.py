from django.db import models

# Create your models here.

class Person(models.Model):
    # active_status=(
    #     ("active","Active"),
    #     ("inactive","Inactive"),
    # )
    
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length = 254)
    # status=models.BooleanField()
    # status=models.CharField(max_length=10,choices=active_status)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Inactive')
