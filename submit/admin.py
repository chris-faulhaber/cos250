from django.contrib import admin
from submit.models import Person, Submission, Line, Assignment, Attendee, TestRunner, Part

# Register your models here.
admin.site.register(Person)
admin.site.register(Submission)
admin.site.register(Line)
admin.site.register(Assignment)
admin.site.register(Attendee)
admin.site.register(TestRunner)
admin.site.register(Part)