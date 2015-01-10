from django.contrib import admin
from django.contrib.auth.models import User
from submit.models import Submission, Line, Assignment, TestRunner, Part, PartGrade

# Register your models here.
admin.site.register(Submission)
admin.site.register(Line)
admin.site.register(Assignment)
admin.site.register(TestRunner)
admin.site.register(Part)