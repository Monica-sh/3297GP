from django.contrib import admin
from .models import PersonalEvent, PublicEvent
# Register your models here.

admin.site.register(PersonalEvent)
admin.site.register(PublicEvent)