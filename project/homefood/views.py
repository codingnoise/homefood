from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import SchedulerForm

from messages.messages import ScheduleMessage
from homefood.constants import InterviewConstants
from homefood.dao.appointments_dao import AppointmentsDao
from common.util.log.Logger import Logger
from homefood.manager.schedule_manager import ScheduleManager
from homefood.manager.task_manager import TaskManager

PAGE_TEMPLATE = "%s:%s"
INDEX_URL = PAGE_TEMPLATE % ("homefood", "index")
LOG = Logger().get_logger()


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

@method_decorator(login_required, name="dispatch")
class ScheduleView(LoginRequiredMixin, ListView):
    template_name = "homefood/schedule.html"
    context_object_name = "availabilities"

    def get_queryset(self):
        return ""

    @method_decorator(login_required(login_url="users/register.html"))
    def dispatch(self, *args, **kwargs):
        return super(ScheduleView, self).dispatch(*args, **kwargs)


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
                print "here"
                schedule = schedule_form.cleaned_data
                date = schedule.get("scheduleDate")
                time = schedule.get("scheduleTime")
                topic = schedule.get("scheduleTopic")
                interviewee_email = request.user.email
                print "date=" + date + " time=" + time + " topic=" + topic
                msg = ScheduleMessage(schedule_date=date, schedule_time=time, schedule_topic=topic, interviewee_email=interviewee_email)
                tm.schedule(msg)
            else:
                print "Schedule form not valid"
            return render(request, self.success_template_name)
        except Exception:
            return render(request, self.success_template_name)

    def get(self, request):
        upcoming_interviews = {"interviews": []}
        try:
            if request.user.is_active:
                user = request.user
                filter = request.GET.get('filter', None)
                if not filter:
                    # get all interviews
                    upcoming_interviews["interviews"] = ["all_interviews"]
                elif filter == InterviewConstants.INTERVIEW_STATUS_SCHEDULED:
                    upcoming_interviews["interviews"] = AppointmentsDao.get_scheduled_interviews(user)
            print upcoming_interviews
            return JsonResponse(upcoming_interviews)
        except Exception:
            LOG.exception("Error occurred duing GET /appointments for user=%s" % request.user)

# def handler404(request):
#     return render(request, '404.html', status=404)


# def handler500(request):
#     return render(request, '500.html', status=500)

############## User ##############

# class AddUser(CreateView):
#     model = User
#     form_class = AddUserForm
#     success_url = reverse_lazy(INDEX_URL)

