from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Food, User, AddUserForm, AddFoodProductForm, Location, AddLocation


PAGE_TEMPLATE = "%s:%s"
INDEX_URL = PAGE_TEMPLATE % ("homefood", "index")


class IndexView(ListView):
    template_name = "homefood/index.html"
    context_object_name = "all_products"

    def get_queryset(self):
        return Food.objects.all()


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
