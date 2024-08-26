from django.contrib import admin
from .models import Candidate

# Register your models here.
class candidate(admin.ModelAdmin):
    list_display = "firstname", "lastname", "email", "phone", "gender", "age", "country", "joined_date"

admin.site.register(Candidate,candidate)
