from django.contrib import admin
from homepage.models import MyFirstModel

# Register your models here.

class MyFirstModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(MyFirstModel, MyFirstModelAdmin)
