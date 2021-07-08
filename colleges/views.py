from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
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
        return redirect('x_admin')
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request,username = username ,password=password)

            if user is not None:
                login(request, user)
                return render(request,'html/admin.html')
            else:
                messages.info(request, 'Username or Password is incorrect.')
                return redirect('login')

        return render(request, 'html/login.html')

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('x_admin')
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

def Compare(request,comp_id):
    comp_data = Colleges_Model.objects.get(id=comp_id)
    Comp_Colg_id = College_Details.objects.filter(college_id=comp_id)
    return render(request, 'html/compare.html',{'colg_id':Comp_Colg_id,'colg_data': comp_data})

def Search_Colg(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venue = Colleges_Model.objects.filter(college_name__contains = searched)
        return render(request, 'html/base1.html',{'searched':searched,'venue':venue})

    else:
        return render(request, 'html/base1.html',{})

@login_required(login_url='login')
def X_Admin(request):
    return render(request,'html/admin.html')
@login_required(login_url='login')
def College_Form(request):
    form = College_Model_Form()
    if request.method == 'POST':
        form = College_Model_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('college_form')
    else:
        form = College_Model_Form()
    context = {"form" : form}
    return render(request, 'html/college_form.html',context)

@login_required(login_url='login')
def Degree_Form(request):
    degree_form = Degree_Model_Form()
    if request.method == 'POST':
        degree_form = Degree_Model_Form(request.POST)
        if degree_form.is_valid():
            degree_form.save()
            return redirect('degree_form')
    else:
        degree_form = Degree_Model_Form()
    context = {"degree_form" : degree_form}
    return render(request, 'html/college_form.html',context)

@login_required(login_url='login')
def Stream_Form(request):
    stream_form = Stream_Model_Form()
    if request.method == 'POST':
        stream_form = Stream_Model_Form(request.POST, request.FILES)
        if stream_form.is_valid():
            stream_form.save()
            return redirect('stream_form')
    else:
        stream_form = Stream_Model_Form()
    context = {"stream_form" : stream_form}
    return render(request, 'html/college_form.html',context)

@login_required(login_url='login')
def Branch_Form(request):
    branch_form = Branch_Model_Form()
    if request.method == 'POST':
        branch_form = Branch_Model_Form(request.POST, request.FILES)
        if branch_form.is_valid():
            branch_form.save()
            return redirect('branch_form')
    else:
        branch_form = Branch_Model_Form()
    context = {"branch_form" : branch_form}
    return render(request, 'html/college_form.html',context)

@login_required(login_url='login')
def Course_Form(request):
    course_form = Course_Model_Form()
    if request.method == 'POST':
        course_form = Course_Model_Form(request.POST, request.FILES)
        if course_form.is_valid():
            course_form.save()
            return redirect('course_form')
    else:
        course_form = Course_Model_Form()
    context = {"course_form" : course_form}
    return render(request, 'html/college_form.html',context)

@login_required(login_url='login')
def College_Details_Form(request):
    form = College_Details_Model_Form()
    if request.method == 'POST':
        college_detail_form = College_Details_Model_Form(request.POST, request.FILES)
        if college_detail_form.is_valid():
            college_detail_form.save()
            return redirect('college_details_form')
    else:
        college_detail_form = College_Details_Model_Form()
    context = {"college_detail_form" : college_detail_form}
    return render(request, 'html/college_form.html',context)






# def College_Form(request):
#     if request.method == 'POST':
#         # if College_Model_Form:        
#         colg_form = College_Model_Form(request.POST or None, request.FILES or None)
#         # elif Degree_Model_Form:        
#         degree_form = Degree_Model_Form(request.POST or None,request.FILES or None)
#         # elif Stream_Model_Form:        
#         stream_form = Stream_Model_Form(request.POST or None,request.FILES or None)
#         # elif Branch_Model_Form:        
#         branch_form = Branch_Model_Form(request.POST or None,request.FILES or None)
#         # elif Course_Model_Form:        
#         cors_form = Course_Model_Form(request.POST or None,request.FILES or None)
#         # elif College_Details_Form:        
#         colg_dtl_form = College_Details_Form(request.POST or None,request.FILES or None)

#         if colg_form.is_valid():
#             colg_form.save()
#         elif degree_form.is_valid():
#             degree_form.save()
#         elif stream_form.is_valid():
#             stream_form.save()
#         elif branch_form.is_valid():
#             branch_form.save()
#         elif cors_form.is_valid():
#             cors_form.save()
#         elif colg_dtl_form.is_valid():
#             colg_dtl_form.save()
#             return redirect('college_form')
#     else:
#         colg_form = College_Model_Form()
#         degree_form = Degree_Model_Form()
#         stream_form = Stream_Model_Form()
#         branch_form = Branch_Model_Form()
#         cors_form = Course_Model_Form()
#         colg_dtl_form = College_Details_Form()
#     context = {"colg_form" : colg_form,"degree_form" : degree_form,"stream_form" : stream_form,"branch_form" : branch_form,"colg_dtl_form" : colg_dtl_form,"cors_form":cors_form}
#     return render(request, 'html/college_form.html',context)
