from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Student
from .forms import AddStudentForm, UpdateStudentForm

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


# update student
def update_student(request, id):

    student = get_object_or_404(Student, pk=id)

    if request.method == "POST":
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student details updated")
            return redirect("student:home")
        else:
            messages.error(request, "Confirm all details are as they should be")
        
    form = UpdateStudentForm(instance=student)

    return render(request, "student/update_student.html", {
        "form":  form
    })


def delete_student(request, id):

    student = get_object_or_404(Student, pk=id)

    student.delete()

    messages.info(request, "Student deleted!!")

    return redirect("student:home")


