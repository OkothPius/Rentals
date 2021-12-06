from django.contrib import admin
from .models import User, Tenant, Agent

admin.site.register(User)
admin.site.register(Tenant)
admin.site.register(Agent)
