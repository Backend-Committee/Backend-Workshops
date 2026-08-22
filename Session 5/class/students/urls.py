from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.students),
    path("courses/", views.courses),
    path("departments/", views.departments),
    path("students/filter/<str:name>/", views.filter_students),
    path("student/<int:id>/", views.student),
    path("student/courses/<int:id>/", views.student_courses),
    path("department/courses/<int:id>/", views.department_courses),
]