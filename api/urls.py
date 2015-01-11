from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.views import *
from api.serializers import AssignmentSerializer
from submit.models import Assignment

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^assignments/$',
        ListAPIView.as_view(queryset=Assignment.objects.all(), serializer_class=AssignmentSerializer),
        name='assignment_list_api'),
    url(r'^assignments/find/(?P<pk>[-_\w]+)/$',
        RetrieveAPIView.as_view(queryset=Assignment.objects.all(), serializer_class=AssignmentSerializer),
        name='assignment_detail_api'),
    url(r'^assignment/grades/find/(?P<id>[-_\w]+)/$', AssignmentGradeView.as_view(), name='assignment_grades_api'),
)
