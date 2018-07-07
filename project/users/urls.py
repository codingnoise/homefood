from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "users"

urlpatterns = [
    url(r'^signup/$', views.SignupView.as_view(), name="signup"),
    url(r'^register/$', views.RegisterView.as_view(), name="register"),
    url(r'^home/$', views.HomeView.as_view(), name="home"),
    url(r'^login/$', views.AuthView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'users/register.html'}, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()


