from django.conf.urls import url
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "homefood"

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r'^about/$', views.AboutView.as_view(), name="about"),
    url(r'^syllabus/$', views.SyllabusView.as_view(), name="syllabus"),
    url(r'^courses/$', views.CoursesView.as_view(), name='courses'),
    url(r'^enroll/$', views.EnrollView.as_view(), name='enroll'),
    url(r'^schedule/$', views.ScheduleView.as_view(), name='schedule'),
    url(r'^ajax/availability/$', views.get_availability, name='get_availability'),
    url(r'^appointment/$', views.AppointmentView.as_view(), name="appointment"),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
]

urlpatterns += staticfiles_urlpatterns()