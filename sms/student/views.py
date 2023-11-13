from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Student
from .forms import AddStudentForm

# display all students
def home(request):
    students = Student.objects.all()

    return render(request, "student/home.html", {
        "students": students,
        "title": "home"
    })


# add a student
def add_student(request):
    form = AddStudentForm()

    if request.method == "POST":
        form = AddStudentForm(request.POST)
        
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            form.save()
            messages.success(request, f"Student: {first_name} {last_name} saved.")

            return redirect("student:home")
        else:
            messages.error(request, "Incorrect Details")
            form = AddStudentForm()

    return render(request, "student/add_student.html", {
        "form": form,
        "title": "add-student",
    })
