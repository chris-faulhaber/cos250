from django.conf.urls import patterns, include, url

from django.contrib import admin
from submit.views import SubmissionDetailView, LoginView, StudentListView, StudentDetailView
from submit.views import AssignmentDetailView, AssignmentListView, AssignmentGradesView
from django.contrib.admin.views.decorators import staff_member_required

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^assignments/$', AssignmentListView.as_view(), name='assignment_list'),
    url(r'^grades/$', staff_member_required(AssignmentGradesView.as_view()), name='assignment_grades_list'),
    url(r'^assignment/(?P<pk>[-_\w]+)/$', AssignmentDetailView.as_view(), name='assignment_detail'),
    url(r'^logout/', 'submit.views.logout_view', name='logout'),
    url(r'^submit/', AssignmentListView.as_view(), name='index'),
    url(r'^submission/(?P<pk>[-_\w]+)/$', SubmissionDetailView.as_view(), name='submission'),
    url(r'^upload/', 'submit.views.upload', name='upload'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^students/$', staff_member_required(StudentListView.as_view()), name='student_list'),
    url(r'^student/grades/(?P<pk>[-_\w]+)/$', staff_member_required(StudentDetailView.as_view()), name='student_grade'),
)
