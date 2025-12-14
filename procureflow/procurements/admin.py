from django.contrib import admin

from .models import ProcurementRequest, RequestItem, StatusLog


admin.site.register(ProcurementRequest)
admin.site.register(RequestItem)
admin.site.register(StatusLog)from .models import User

admin.site.register(User)

