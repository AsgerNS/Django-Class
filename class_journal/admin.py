from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Class, Student, Subject, Grade


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'students'


class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,)


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Grade)

