from django.contrib import admin
from .models import user_tasks,user_tasks_log

admin.site.register(user_tasks)
admin.site.register(user_tasks_log)