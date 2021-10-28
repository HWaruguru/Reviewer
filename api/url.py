from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/profile/$', views.ProfileList.as_view())
]