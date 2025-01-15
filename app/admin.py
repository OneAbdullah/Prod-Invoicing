from django.contrib import admin
from .models import invoice_owner,user_profile,user_permission

admin.site.register(invoice_owner)
admin.site.register(user_profile)
#admin.site.register(user_permission)