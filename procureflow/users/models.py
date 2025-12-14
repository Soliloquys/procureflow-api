from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        ENGINEER = 'ENGINEEER', 'Engineer'
        PROCUREMENT_OFFICER = 'PROCUREMENT_OFFICER', 'Procurement Officer'
        ACCOUNTANT = 'ACCOUNTANT', 'Accountant'
        PROJECT_MANAGER = 'PROJECT_MANAGER', 'Project Manager'

    role = models.CharField(
            max_length=30,
            choices=Role.choices,
            default=Role.ENGINEER, 
        )

    phone = models.CharField(
            max_length=15, 
            blank=True, 
            null=True
        )
    def __str__(self):
            return f"{self.username} ({self.role})"
