from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homefood/', include('homefood.urls')),
    url(r'^user/', include('users.urls'))
]
