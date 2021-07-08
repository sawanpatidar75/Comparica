from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class College_Model_Form(forms.ModelForm):
    class Meta:
        model = Colleges_Model
        fields = '__all__'

class Degree_Model_Form(forms.ModelForm):
    class Meta:
        model = Degree_Model
        fields = ['degree']
        labels = {'degree' : 'Enter Degree'}

class Stream_Model_Form(forms.ModelForm):
    class Meta:
        model = Stream_Model
        fields = '__all__'

class Branch_Model_Form(forms.ModelForm):
    class Meta:
        model = Branch_Model
        fields = '__all__'

class Course_Model_Form(forms.ModelForm):
    class Meta:
        model = Course_Model
        fields = '__all__'

class College_Details_Model_Form(forms.ModelForm):    
    class Meta:
        model = College_Details
        fields = '__all__'



