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


    #----- food stuff ----
    url(r'^cook/$', views.AddUser.as_view(), name="add-user"),
    url(r'^food/$', views.AddFood.as_view(), name="add-food"),
    url(r'^location/$', views.AddLocation.as_view(), name="add-location")
    #---------------------
]

urlpatterns += staticfiles_urlpatterns()