from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Food, User, AddUserForm, AddFoodProductForm, Location, AddLocation


PAGE_TEMPLATE = "%s:%s"
INDEX_URL = PAGE_TEMPLATE % ("homefood", "index")


class IndexView(ListView):
    template_name = "homefood/interview.html"
    #context_object_name = "all_products"

    def get_queryset(self):
        return ""

class AboutView(ListView):
    template_name = "homefood/about.html"
    #context_object_name = "all_products"

    def get_queryset(self):
        return ""

class SyllabusView(ListView):
    template_name = "homefood/syllabus.html"
    #context_object_name = "all_products"

    def get_queryset(self):
        return ""

class EnrollView(ListView):
    template_name = "homefood/enroll.html"
    #context_object_name = "all_products"

    def get_queryset(self):
        return ""

class CoursesView(ListView):
    template_name = "homefood/courses.html"
    #context_object_name = "all_products"

    def get_queryset(self):
        return ""

############## User ##############

class AddUser(CreateView):
    model = User
    form_class = AddUserForm
    success_url = reverse_lazy(INDEX_URL)


class UpdateUserView(UpdateView):
    model = User
    form_class = AddUserForm
    success_url = reverse_lazy(INDEX_URL)


class DeleteUserView(DeleteView):
    model = User
    success_url = reverse_lazy(INDEX_URL)


############## Food ##############

class AddFood(CreateView):
    model = Food
    form_class = AddFoodProductForm
    success_url = reverse_lazy(INDEX_URL)


class AddLocation(CreateView):
    model = Location
    form_class = AddLocation
    success_url = reverse_lazy(INDEX_URL)
