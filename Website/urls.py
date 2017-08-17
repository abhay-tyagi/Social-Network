from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register.as_view(), name='register'),
    url(r'^show_profile/(?P<pk>\d+)$', views.show_profile, name='show_profile'),
    url(r'^post/$', views.AddPost.as_view(), name='post'),
    url(r'^likepost/(?P<postid>\d+)$', views.likepost, name='likepost'),
]