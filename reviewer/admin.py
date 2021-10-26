from django.contrib import admin
from .models import Rating, Project, Profile

admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(Project)