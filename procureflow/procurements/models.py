from django.db import models
from projects.models import Project
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ProcurementRequest(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        PENDING_APPROVAL = 'PENDING_APPROVAL', 'Pending Approval'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'


    reference = models.CharField(max_length=50, unique=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='procurement_requests')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    urgency = models.CharField(max_length=50)
    purpose = models.TextField()

    rejection_reason = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference_code
    

class RequestItem(models.Model):
    procurement_request = models.ForeignKey(ProcurementRequest, on_delete=models.CASCADE, related_name='items')
    item_description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    selected_vendor = models.ForeignKey('vendors.Vendor', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def total_cost(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.item_description
    

class StatusLog(models.Model):
    procurement_request = models.ForeignKey(
    ProcurementRequest,
    on_delete=models.CASCADE,
    related_name='status_logs'
)

    status = models.CharField(max_length=30)
    actor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
        )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.procurement_request.reference_code} - {self.status}"

