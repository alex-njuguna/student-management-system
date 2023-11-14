from django.urls import path

from . import views


app_name = "student"


urlpatterns = [
    path("", views.home, name="home"),
    path("add_student/", views.add_student, name="add_student"),
    path("update_student/", views.update_student, name="update_student"),
    path("delete_student/", views.delete_student, name="delete_student"),
]