from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views
from .views import get_household_data, highDeltaChartData, lowDeltaChartData

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^case_study/$', views.case_study, name='case_study'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^data/$', views.data, name='contact'),
    url(r'^api/chart/highDeltaScatter/$', highDeltaChartData.as_view()),
    url(r'^api/chart/lowDeltaScatter/$', lowDeltaChartData.as_view()),
    url(r'^api/data/(?P<household_id>.+)/$', get_household_data, name='api-data'),
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('main_site/img/favicon.ico'),), name="favicon"),
]