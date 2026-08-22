from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Course, Department
# Create your views here.


# Get all students
def students(request):
    data = Student.objects.all()
    return JsonResponse({"students": list(data.values())})


# Get all courses
def courses(request):
    data = Course.objects.all()
    return JsonResponse({"courses": list(data.values())})


# Get all departments
def departments(request):
    data = Department.objects.all()
    return JsonResponse({"departments": list(data.values())})


# Filter students
def filter_students(request,name):
    data = Student.objects.filter(name=name)
    return JsonResponse({"students": list(data.values())})


# Get one student
def student(request,id):
    data = Student.objects.get(id=id)
    return JsonResponse({"student": data.name})


# Student → Courses
def student_courses(request,id):
    student = Student.objects.get(id=id)
    return JsonResponse({
        "courses": list(student.courses.values())
    })


# Department → Courses
def department_courses(request,id):
    department = Department.objects.get(id=id)
    return JsonResponse({
        "courses": list(department.courses.values())
    })