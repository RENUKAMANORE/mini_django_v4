from django.contrib import admin
from .models import Portal, Title,JobDescription,Applicant

# Register your models here.
admin.site.register(Portal)
admin.site.register(Title)
admin.site.register(JobDescription)
admin.site.register(Applicant)


