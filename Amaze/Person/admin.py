from django.contrib import admin
from Person.models import Person

# Register your models here.
class Person_Admin(admin.ModelAdmin):
    #列表显示字段
    list_display = ('email','mobilephone','username','age','createdate')
    #查询字段
    search_fields = ('email','mobilephone','username')
    #超连接
    list_display_links = ('email','mobilephone','username')
    #时间条件
    date_hierarchy = 'createdate'
    #每页条数
    list_per_page = 1
    #只读字段
    readonly_fields = ('createdate','modifydate')

admin.site.register(Person,Person_Admin)

admin.site.header='学生管理系统'
admin.site.title='学生管理系统'
