from django.contrib import admin
from .models import Feedback
from .models import Products

admin.site.register(Feedback)
# Register your models here.
admin.site.register(Products)