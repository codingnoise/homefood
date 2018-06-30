from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View


from .models import SchedulerForm

from messages.messages import ScheduleMessage
from manager import ScheduleManager, TaskManager

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

class ScheduleView(ListView):
    template_name = "homefood/schedule.html"
    context_object_name = "availabilities"

    def get_queryset(self):
        return ""

def get_availability(request):
    date = request.GET.get("date", None)
    scheduler = ScheduleManager()
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

class ErrorView(ListView):
    template_name = "homefood/error.html"
    #context_object_name = "all_products"

    def get_queryset(self):
        return ""

class AppointmentView(View):
    success_template_name = "homefood/success.html"
    error_template_name = "homefood/error.html"

    def post(self, request):
        try:
            schedule_form = SchedulerForm(request.POST)
            tm = TaskManager()
            # HACK - Starting our task manager on the first request for scheduling
            # Use celery + Rabbitmq instead.
            if not tm.is_running():
                tm.run()

            if schedule_form.is_valid():
                schedule = schedule_form.cleaned_data
                date = schedule.get("scheduleDate")
                time = schedule.get("scheduleTime")
                topic = schedule.get("scheduleTopic")
                email = schedule.get("email")
                print "date=" + date + " time=" + time + " topic=" + topic
                msg = ScheduleMessage(schedule_date=date, schedule_time=time, schedule_topic=topic, email=email)
                tm.schedule(msg)
            return render(request, self.success_template_name)
        except Exception:
            return render(request, self.success_template_name)



# def handler404(request):
#     return render(request, '404.html', status=404)


# def handler500(request):
#     return render(request, '500.html', status=500)

############## User ##############

# class AddUser(CreateView):
#     model = User
#     form_class = AddUserForm
#     success_url = reverse_lazy(INDEX_URL)

