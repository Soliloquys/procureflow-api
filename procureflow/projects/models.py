from django.db import models

class Project(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        COMPLETED = 'COMPLETED', 'Completed'
        ON_HOLD = 'ON_HOLD', 'On Hold'

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    total_budget = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        default = 0.00
    )
    
    spent_amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        default = 0.00
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location} ({self.status})"