from django.contrib import admin
from django.contrib.auth.models import User
from submit.models import Submission, Line, Assignment, TestRunner, Part, PartGrade, AssignmentGrade


class AssignmentGradeAdmin(admin.TabularInline):
    model = AssignmentGrade
    extra = 0
    readonly_fields = ('grade', 'user', )


class AssignmentAdmin(admin.ModelAdmin):
    inlines = [AssignmentGradeAdmin, ]


admin.site.register(Submission)
admin.site.register(Line)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(TestRunner)
admin.site.register(Part)