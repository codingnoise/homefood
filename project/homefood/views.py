from django.shortcuts import render
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View


from .models import Food, User, AddUserForm, AddFoodProductForm, Location, AddLocation, SchedulerForm

from messages.messages import ScheduleMessage
from manager import SchedulerManager, TaskManager

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

class ContactView(ListView):
    template_name = "homefood/contact.html"
    context_object_name = "availabilities"

    def get_queryset(self):
        return ""

def get_availability(request):
    date = request.GET.get("date", None)
    scheduler = SchedulerManager()
    availability = scheduler.get_availability(date)
    result = {
        "availability": availability
    }
    return JsonResponse(result)


class SuccessView(ListView):
    template_name = "homefood/success.html"
    #context_object_name = "all_products"

    def get_queryset(self):
        return ""

class SchedulerView(View):
    success_template_name = "homefood/success.html"

    def post(self, request):
        schedule_form = SchedulerForm(request.POST)
        tm = TaskManager()
        # HACK - Starting our task manager on the first request for scheduling
        # Use celery + Rabbitmq instead.
        if not tm.is_running():
            tm.run()

        if schedule_form.is_valid():
            manager = SchedulerManager()
            schedule = schedule_form.cleaned_data
            date = schedule.get("scheduleDate")
            time = schedule.get("scheduleTime")
            email = schedule.get("email")
            print "date=" + date + " time=" + time
            msg = ScheduleMessage(schedule_date=date, schedule_time=time, email=email)
            tm.schedule(msg)
            print str(schedule)

        return render(request, self.success_template_name)


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
