from django.contrib import admin

# Register your models here.
from .models import Nursing, Welding, Driving, Development

admin.site.register(Nursing)
admin.site.register(Welding)
admin.site.register(Driving)
admin.site.register(Development)