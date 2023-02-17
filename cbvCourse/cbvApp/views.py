from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cbvApp.models import Course
from django.urls import reverse_lazy

# Create your views here.
class CourseListView(ListView):
    model = Course

class CourseDetail(DetailView):
    model = Course

class CourseCreateView(CreateView):
    model = Course
    fields = ('name', 'description', 'instructor', 'rating')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ('name', 'description', 'instructor', 'rating',)

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses')
