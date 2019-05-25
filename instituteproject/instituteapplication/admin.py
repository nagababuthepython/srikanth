from django.contrib import admin
from .models import CoursesData
class AdminCourseData(admin.ModelAdmin):
    list_display = ['course_id',
                    'course_name',
                    'course_duration',
                    'course_fee',
                    'course_date',
                    'course_time',
                    'course_trainer_name',
                    'trainer_exp']
admin.site.register(CoursesData,AdminCourseData)