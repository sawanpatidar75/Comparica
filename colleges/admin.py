from django.contrib import admin
from . models import *

admin.site.register(Colleges_Model)
admin.site.register(Degree_Model)
admin.site.register(Stream_Model)
admin.site.register(Branch_Model)

class Admin_Course_Model(admin.ModelAdmin):
    list_display = ['course_name','degree','stream','branch']
admin.site.register(Course_Model,Admin_Course_Model)

class Admin_College_Detail(admin.ModelAdmin):
    list_display = ['college','course','fee']
admin.site.register(College_Details,Admin_College_Detail)























# from .models import Colleges_Model,Course_Branch,Course_Degree,Course_Field,Course,Course_Fee,Admission_Type

# Register your models here.

# class AdminColleges_Model(admin.ModelAdmin):
#     list_display = ['college_name','college_address']

# class AdminCourse_Branch(admin.ModelAdmin):
#     list_display = ['course_branch']

# class AdminCourse_Degree(admin.ModelAdmin):
#     list_display = ['course_degree']

# class AdminCourse_Field(admin.ModelAdmin):
#     list_display = ['course_field']

# class AdminCourse(admin.ModelAdmin):
#     list_display = ['colleges','branch','field']

# class AdminCourse_Fee(admin.ModelAdmin):
#     list_display = ['college_select','course_select']

# class AdminAdmission_Type(admin.ModelAdmin):
#     list_display = ['type_of_admission']

    

# admin.site.register(Colleges_Model)
# admin.site.register(Course_Branch)
# admin.site.register(Course_Degree)
# admin.site.register(Course_Field)
# admin.site.register(Course)
# admin.site.register(Course_Fee)
# admin.site.register(Admission_Type)
