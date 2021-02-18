from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(CustomUser)
admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Parents)
admin.site.register(Module)
admin.site.register(Courses)
admin.site.register(CoursesPaid)
admin.site.register(Payment)
admin.site.register(Subjects)
admin.site.register(StudentNotification)
admin.site.register(TeacherNotification)
admin.site.register(Completed_course)
admin.site.register(Completed_module)





