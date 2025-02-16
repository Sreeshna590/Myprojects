from django.shortcuts import render
from app1.forms import SchoolForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy  # Import reverse_lazy for success_url
from .models import School, Student  # Import the School and Student models

# Class-based view for the home page
class Home(TemplateView):
    template_name = 'home.html'

# Class-based view for adding a new school
class AddSchool(CreateView):
    model = School
    template_name = "addschool.html"  # Ensure this file exists in your templates directory
    form_class = SchoolForm
    success_url = reverse_lazy('home')  # Ensure 'home' is a valid URL name in your urls.py

# Class-based view for adding a new student
class AddStudent(CreateView):
    model = Student
    template_name = "addstudent.html"  # Ensure this file exists in your templates directory
    fields = ['name', 'age', 'school']  # Ensure these fields exist in the Student model
    success_url = reverse_lazy('home')  # Ensure 'home' is a valid URL name in your urls.py
