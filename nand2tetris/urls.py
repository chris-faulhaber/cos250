from django.conf.urls import patterns, include, url

from django.contrib import admin
from submit.views import SubmissionDetailView, SubmissionListView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^submit/', 'submit.views.index', name='index'),
    url(r'^submissions/', SubmissionListView.as_view(), name='submitted'),
    url(r'^submission/(?P<pk>[-_\w]+)/$', SubmissionDetailView.as_view(), name='submission'),
    url(r'^upload/', 'submit.views.upload', name='upload'),
    url(r'^admin/', include(admin.site.urls)),
)
