from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<homework_sheet_id>[0-9]+)/$', views.assignment, name='assignment'),
]