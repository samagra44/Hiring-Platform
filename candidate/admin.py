from django.contrib import admin
from candidate import models

@admin.register(models.MyApplyJobList)
class MyApplyJobListAdmin(admin.ModelAdmin):
    list_display = ('id','user','job','dateYouApply')

@admin.register(models.IsSortList)
class IsSortListAdmin(admin.ModelAdmin):
    list_display = ('id','user','job','dateYouApply')


