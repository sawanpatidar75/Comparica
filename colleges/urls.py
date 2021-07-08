from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='indexurl'),
    path('coll',views.colleges,name='coll'),
    path('details/<int:pid>',views.college_detail,name='details'),

    path('colg_exp',views.college_data,name='colg_exp'),
    path('Colgid/<int:pid>',views.CollegeId,name='Colgid'),
    path('show_courses/<int:show_id>',views.Show_Courses,name='show_courses'),
    path('course_college/<int:cors_id>',views.print_course_college,name='course_college'),
    path('compare_colg/<int:comp_id>',views.Compare,name='compare_colg'),
    path('search-colg',views.Search_Colg,name='search-colg'),
    path('login',views.LogIn,name='login'),
    path('signup',views.SignUp,name='signup'),
    path('logout',views.LogOut,name='logout'),
    path('logedin',views.LogedIn,name='logedin'),

    path('x_admin',views.X_Admin,name='x_admin'),
    path('college_form',views.College_Form,name='college_form'),
    path('degree_form',views.Degree_Form,name='degree_form'),
    path('stream_form',views.Stream_Form,name='stream_form'),
    path('branch_form',views.Branch_Form,name='branch_form'),
    path('course_form',views.Course_Form,name='course_form'),
    path('college_details_form',views.College_Details_Form,name='college_details_form'),




    # path('Dropdown_Course',views.course_detail,name='Dropdown_Cors'),

    # path('sidenav',views.side_nav)

] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
