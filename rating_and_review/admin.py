from django.contrib import admin
from .models import RatingAndReviewModel
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile_no']
    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(RatingAndReviewModel,FeedbackAdmin)
