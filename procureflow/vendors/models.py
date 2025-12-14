from django.db import models

from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
