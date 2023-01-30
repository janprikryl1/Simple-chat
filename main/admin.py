from django.contrib import admin
from .models import Message
# Register your models here.
admin.site.site_header = 'Adminovo'
admin.site.register(Message)
# Register your models here.
