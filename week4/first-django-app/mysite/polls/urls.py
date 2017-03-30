from django.conf.urls import url

from . import views

app_name = "polls"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/example/$', views.example, name='example'),
    url(r'^(?P<question_id>[0-9]+)/api/$', views.api, name='api'),
    url(r'^api_save/$', views.api_save, name='api'),
]
