from django.contrib import admin

# Register your models here.
from .models import Skill,JobApplication,Feedback,Factor

admin.site.register(Skill)
admin.site.register(JobApplication)
admin.site.register(Feedback)
admin.site.register(Factor)