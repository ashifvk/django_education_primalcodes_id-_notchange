from django.contrib import admin
from .models import Candidate,Education,todo

# Register your models here.
admin.site.register(Candidate)
class educationAdmin(admin.ModelAdmin):
    list_display=('id','course','university','year','reg_id')
admin.site.register(Education,educationAdmin)

class todoAdmin(admin.ModelAdmin):
    list_display=('id','player','club','value')
admin.site.register(todo,todoAdmin)