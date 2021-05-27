from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# from .models import Colleges_Model,Course_Branch,Course_Degree,Course_Field,Course,Course_Fee,Admission_Type

# Create your views here.

def index(request):
    data = Colleges_Model.objects.all()
    return render(request, 'html/index.html',{'c_data':data})

def colleges(request):
    college =Colleges_Model.objects.all()
    return render(request,'html/college.html',{'colleges':college})

def college_detail(request,pid):
    data = College_Details.objects.get(id=pid)
    return render(request,'html/base1.html',{'colg_data': data})


def college_data(request):
    Colg_data = Colleges_Model.objects.all()
    return render(request, 'html/Colgdata.html',{'colg_data':Colg_data})

def CollegeId(request,pid):
    data = Colleges_Model.objects.get(id=pid)
    Colg_id = College_Details.objects.filter(college_id=pid)
    return render(request, 'html/base1.html',{'colg_id':Colg_id,'colg_data': data})

def course_detail(request):
    degree_data = Degree_Model.objects.all()
    return {'drop_data':degree_data}

def Show_Courses(request,show_id):
    corse_var = Course_Model.objects.filter(degree_id=show_id)
    return render(request, 'html/courses.html',{'course_data':corse_var })


def print_course_college(request,cors_id):
    p_data = College_Details.objects.filter(course_id=cors_id)
    return render(request,'html/print_courses.html',{'colg_data':p_data})

def Compare(request):

    return render(request,'http/compare.html')





