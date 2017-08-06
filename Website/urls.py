from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show_profile/$', views.show_profile, name='show_profile'),
]