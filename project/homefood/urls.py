from django.conf.urls import url
from . import views

app_name = "homefood"

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r'^cook/$', views.AddUser.as_view(), name="add-user"),
    url(r'^food/$', views.AddFood.as_view(), name="add-food"),
    url(r'^location/$', views.AddLocation.as_view(), name="add-location")
]