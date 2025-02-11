from django.contrib import admin
from .models import AccountModel
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']
    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(AccountModel,AccountAdmin)
