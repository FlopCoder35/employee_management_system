from django.contrib import admin
from .models import Member,role,department
# Register your models here.
admin.site.register(Member)
admin.site.register(role)
admin.site.register(department)