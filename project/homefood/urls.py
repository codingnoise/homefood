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
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^ajax/availability/$', views.get_availability, name='get_availability'),
    url(r'^schedule/$', views.SchedulerView.as_view(), name="schedule"),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),


    # #----- food stuff ----
    # url(r'^cook/$', views.AddUser.as_view(), name="add-user"),
    # url(r'^food/$', views.AddFood.as_view(), name="add-food"),
    # url(r'^location/$', views.AddLocation.as_view(), name="add-location")
    # #---------------------
]

urlpatterns += staticfiles_urlpatterns()