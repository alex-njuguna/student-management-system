from django import forms

from .models import Student


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["reg_no", "first_name", "last_name", "email", "course", "gpa"]

        labels = {
            "reg_no": "Registration Number: ", 
            "first_name": "First Name: ", 
            "last_name": "Last Name: ", 
            "email": "Email",
            "course": "Course: ", 
            "gpa": "GPA: "
        }

        widgets = {
            "reg_no": forms.NumberInput(attrs={"class": "form-control"}), 
            "first_name": forms.TextInput(attrs={"class": "form-control"}), 
            "last_name": forms.TextInput(attrs={"class": "form-control"}), 
            "email": forms.EmailInput(attrs={"class": "form-control"}), 
            "course": forms.TextInput(attrs={"class": "form-control"}), 
            "gpa": forms.NumberInput(attrs={"class": "form-control"})
        }


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["reg_no", "first_name", "last_name", "email", "course", "gpa"]

        labels = {
            "reg_no": "Registration Number: ", 
            "first_name": "First Name: ", 
            "last_name": "Last Name: ", 
            "email": "Email",
            "course": "Course: ", 
            "gpa": "GPA: "
        }

        widgets = {
            "reg_no": forms.NumberInput(attrs={"class": "form-control"}), 
            "first_name": forms.TextInput(attrs={"class": "form-control"}), 
            "last_name": forms.TextInput(attrs={"class": "form-control"}), 
            "email": forms.EmailInput(attrs={"class": "form-control"}), 
            "course": forms.TextInput(attrs={"class": "form-control"}), 
            "gpa": forms.NumberInput(attrs={"class": "form-control"})
        }


        