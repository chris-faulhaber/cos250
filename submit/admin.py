from django.contrib import admin
from submit.models import Submission, Line, Assignment, TestRunner, Part


admin.site.register(Submission)
admin.site.register(Line)
admin.site.register(Assignment)
admin.site.register(TestRunner)
admin.site.register(Part)