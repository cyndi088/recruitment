from django.contrib import admin
from jobs.models import Job
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.site_title = '祐全招聘后台管理系统'  # 页面标题

admin.site.site_header = '招聘管理'  # 登录页导航条和首页导航条标题

admin.site.index_title = '欢迎登录'  # 主页标题

admin.site.register(Job, JobAdmin)
