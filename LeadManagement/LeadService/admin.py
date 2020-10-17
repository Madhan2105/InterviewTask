from django.contrib import admin
from .models import LeadModel,FollowUpModel
# Register your models here.
admin.site.register(LeadModel)
admin.site.register(FollowUpModel)
