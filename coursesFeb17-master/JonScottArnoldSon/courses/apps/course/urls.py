from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^course/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^deleted/(?P<id>\d+)$', views.deleted),
    url(r'^comments$', views.comments),
    url(r'^comments/(?P<id>\d+)$', views.comments),
    url(r'^process2/(?P<id>\d+)$', views.process2),

]
