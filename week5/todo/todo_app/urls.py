from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^task/(?P<task_id>[0-9]+)', views.task, name='task'),
    url(r'^status/(?P<status_id>[0-9]+)', views.status, name='status'),
]
