from django.contrib import admin

# Register your models here.
from .models import GitHubRepo
admin.site.register(GitHubRepo)
