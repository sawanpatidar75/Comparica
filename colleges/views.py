from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from .models import Colleges_Model,Course_Branch,Course_Degree,Course_Field,Course,Course_Fee,Admission_Type

# Create your views here.

def index(request):
    data = Colleges_Model.objects.all()
    return render(request, 'html/index.html',{'c_data':data})


def LogIn(request):
    if request.user.is_authenticated:
        return redirect('logedin')
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request,username = username ,password=password)

            if user is not None:
                login(request, user)
                return redirect('logedin')
            else:
                messages.info(request, 'Username or Password is incorrect.')
                return redirect('login')

        return render(request, 'html/login.html')

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('logedin')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Accoutn Created" + user)
                return redirect('login')
        context = {"form" : form}
        return render(request, 'html/signup.html',context)

@login_required(login_url='login')
def LogOut(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def LogedIn(request):
    context = {}
    return render(request,'html/userlogin.html',context)

@login_required(login_url='login')
def colleges(request):
    college =Colleges_Model.objects.all()
    return render(request,'html/college.html',{'colleges':college})

@login_required(login_url='login')
def college_detail(request,pid):
    data = College_Details.objects.get(id=pid)
    return render(request,'html/base1.html',{'colg_data': data})


@login_required(login_url='login')
def college_data(request):
    Colg_data = Colleges_Model.objects.all()
    return render(request, 'html/Colgdata.html',{'colg_data':Colg_data})

@login_required(login_url='login')
def CollegeId(request,pid):
    data = Colleges_Model.objects.get(id=pid)
    Colg_id = College_Details.objects.filter(college_id=pid)
 
    return render(request, 'html/base1.html',{'colg_id':Colg_id,'colg_data': data})

def course_detail(request):
    degree_data = Degree_Model.objects.all()
    return {'drop_data':degree_data}

@login_required(login_url='login')
def Show_Courses(request,show_id):
    corse_var = Course_Model.objects.filter(degree_id=show_id)
    return render(request, 'html/courses.html',{'course_data':corse_var })


def print_course_college(request,cors_id):
    p_data = College_Details.objects.filter(course_id=cors_id)
    return render(request,'html/print_courses.html',{'colg_data':p_data})

@login_required(login_url='login')
def Compare(request,comp_id):
    comp_data = Colleges_Model.objects.get(id=comp_id)
    Comp_Colg_id = College_Details.objects.filter(college_id=comp_id)
    return render(request, 'html/compare.html',{'colg_id':Comp_Colg_id,'colg_data': comp_data})

@login_required(login_url='login')
def Search_Colg(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venue = Colleges_Model.objects.filter(college_name__contains = searched)
        return render(request, 'html/base1.html',{'searched':searched,'venue':venue})

    else:
        return render(request, 'html/base1.html',{})







