from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import get_data, ChartData

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^case_study/$', views.case_study, name='case_study'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^api/data/$', get_data, name='api-data'),
]