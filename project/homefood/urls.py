from django.conf.urls import url
from . import views

app_name = "homefood"

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r'^cook/$', views.AddUser.as_view(), name="add-user")
]