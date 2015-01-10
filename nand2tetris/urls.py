from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from submit.views import SubmissionDetailView, SubmissionListView, LoginView, AssignmentDetailView, AssignmentListView, \
    StudentListView, StudentGradeView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^assignments/$', AssignmentListView.as_view(), name='assignment_list'),
    url(r'^assignment/(?P<pk>[-_\w]+)/$', AssignmentDetailView.as_view(), name='assignment_detail'),
    url(r'^logout/', 'submit.views.logout_view', name='logout'),
    url(r'^submit/', 'submit.views.index', name='index'),
    url(r'^submissions/', login_required(SubmissionListView.as_view()), name='submitted'),
    url(r'^submission/(?P<pk>[-_\w]+)/$', login_required(SubmissionDetailView.as_view()), name='submission'),
    url(r'^upload/', 'submit.views.upload', name='upload'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/$', staff_member_required(StudentListView.as_view()), name='student_list'),
    url(r'^student/grades/(?P<pk>[-_\w]+)/$', staff_member_required(StudentGradeView.as_view()), name='student_grade'),


)
