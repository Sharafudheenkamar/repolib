from myapp.views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('place/', place, name='place'),
    path('homeview/', homeview.as_view(), name='homeview'),
    path('placeview/', placeview.as_view(), name='placeview'),
    path('', indexview.as_view(), name='indexview'),
    path('about/', aboutview.as_view(), name='aboutview'),
    path('contact_us/', contactview.as_view(), name='contactview'),
    path('student/', studentview.as_view(), name='studentview'),
    path('student/add/', studentcreate.as_view(), name='student_create'),
    path('student/delete/<int:id>/', deleteStudent.as_view(), name='deletestudent'),
    path('employee/', employeeview.as_view(), name='employeeview'),
    path('details/', detailsview.as_view(), name='detailsview'),
    # path('employee/edit/<int:id>/', employeedit.as_view(), name='employee_edit'),
    # path('employee_delete/<int:id>/', employeedelete.as_view(), name='employeedelete'),
    path('employeedelete/<int:id>',employeedelete.as_view(),name='employeedelete'),
    path('teacher/', teacherdetails.as_view(), name='teacher_list'),
    path('teacher/add/', teachercreate.as_view(), name='teacher_create'),
    path('teacher/delete/<int:id>/', deleteteacher.as_view(), name='teacher_delete'),

    path('employeeedit/<int:id>/',employeeedit.as_view(),name='employeeedit/')
]