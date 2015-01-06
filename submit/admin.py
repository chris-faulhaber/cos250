from django.contrib import admin
from submit.models import Person, Submission, Line, Course, Assignment, Attendee

# Register your models here.
admin.site.register(Person)
admin.site.register(Submission)
admin.site.register(Line)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Attendee)