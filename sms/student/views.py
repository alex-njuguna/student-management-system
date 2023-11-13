from django.shortcuts import render

from .models import Student

# display all students
def home(request):
    students = Student.objects.all()

    return render(request, "student/home.html", {
        "students": students,
        "title": "home"
    })
