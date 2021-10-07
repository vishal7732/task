from django.contrib import admin

from .models import Address, Orders


# Register your models here.
admin.site.register(Address)
admin.site.register(Orders)