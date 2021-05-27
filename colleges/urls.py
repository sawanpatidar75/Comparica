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
    path('compare',views.Compare,name='compare'),


    # path('Dropdown_Course',views.course_detail,name='Dropdown_Cors'),

    # path('sidenav',views.side_nav)

] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
