from django.contrib import admin
from .models import Client, Rendezvous, Consultation
# Register your models here.


admin.site.register(Client)
admin.site.register(Rendezvous)
admin.site.register(Consultation)