from django.db import models

# Create your models here.


class Colleges_Model(models.Model):
    college_name = models.CharField(max_length=50)
    college_address= models.CharField(max_length=100)
    college_image = models.ImageField(upload_to='College_Images')
    def __str__(self):
        return self.college_name

class Degree_Model(models.Model):
    degree = models.CharField(max_length=50)
    def __str__(self):
        return self.degree

class Stream_Model(models.Model):
    stream = models.CharField(max_length=50)
    def __str__(self):
        return self.stream
    

class Branch_Model(models.Model):
    branch = models.CharField(max_length=50)
    def __str__(self):
        return self.branch
    

class Course_Model(models.Model):
    course_name = models.CharField(max_length=50)
    degree = models.ForeignKey(Degree_Model, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream_Model, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch_Model, on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name
    

class College_Details(models.Model):
    college = models.ForeignKey(Colleges_Model, on_delete= models.CASCADE)
    course = models.ForeignKey(Course_Model,on_delete=models.CASCADE)
    fee = models.IntegerField()
    def __str__(self):
        return self.college.college_name

    





# class Course_Degree(models.Model):
#     course_degree = models.CharField(max_length=30)
#     def __str__(self):
#         return self.course_degree

# class Course_Field(models.Model):
#     course_field = models.CharField(max_length=30)
#     def __str__(self):
#         return self.course_field

# class Course_Branch(models.Model):
#     course_branch = models.CharField(max_length=20)
#     def __str__(self):
#         return self.course_branch

# class Course(models.Model):
#     name = models.CharField(max_length=20, default=0)
#     degree = models.ForeignKey(Course_Degree, on_delete=models.CASCADE)
#     field = models.ForeignKey(Course_Field, on_delete=models.CASCADE)
#     branch = models.ForeignKey(Course_Branch, on_delete=models.CASCADE)
#     colleges = models.ManyToManyField(Colleges_Model)
#     def __str__(self):
#         return self.name
    

# class Admission_Type(models.Model):
#     type_of_admission = models.CharField(max_length=50)
#     def __str__(self):
#         return self.type_of_admission
    


# class Course_Fee(models.Model):
#     college_select = models.ForeignKey(Colleges_Model, on_delete=models.CASCADE)
#     course_select = models.ForeignKey(Course,on_delete=models.CASCADE)
#     course_fee = models.IntegerField()







