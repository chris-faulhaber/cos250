from django.contrib import admin
from django.contrib.auth.models import User
from submit.models import Submission, Line, Assignment, TestRunner, Part, AssignmentGrade, PartGrade
from import_export.admin import ImportExportModelAdmin
from submit.resources import AssignmentGradeResource, PartGradeResource


class AssignmentGradeAdmin(ImportExportModelAdmin):
    resource_class = AssignmentGradeResource
    list_display = ('get_assignment', 'grade', 'get_user')
    list_filter = ('assignment', )

    def get_user(self, obj):
        return "{0} {1}".format(obj.user.first_name, obj.user.last_name)

    def get_assignment(self, obj):
        return obj.assignment.description

    get_assignment.short_description = 'Assignment Name'
    get_user.short_description = 'Student Name'


class PartGradeAdmin(ImportExportModelAdmin):
    resource_class = PartGradeResource
    list_display = ('get_assignment', 'current_score', 'get_user', 'part')
    list_filter = ('part__assignment', )

    def get_user(self, obj):
        return "{0} {1}".format(obj.user.first_name, obj.user.last_name)

    def get_assignment(self, obj):
        return obj.part.assignment.description

    get_assignment.short_description = 'Assignment Name'
    get_user.short_description = 'Student Name'

admin.site.register(PartGrade, PartGradeAdmin)
admin.site.register(Submission)
admin.site.register(Line)
admin.site.register(Assignment)
admin.site.register(AssignmentGrade, AssignmentGradeAdmin)
admin.site.register(TestRunner)
admin.site.register(Part)