__author__ = 'Craig'

from django.contrib import admin
from models import User, Demographic, Experience

admin.site.register(Demographic)
admin.site.register(Experience)
