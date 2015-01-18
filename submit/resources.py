from import_export import resources
from submit.models import AssignmentGrade, PartGrade


class AssignmentGradeResource(resources.ModelResource):
    class Meta:
        model = AssignmentGrade
        fields = ('user__first_name', 'user__last_name', 'grade')


class PartGradeResource(resources.ModelResource):
    class Meta:
        model = PartGrade
        fields = ('user__first_name', 'user__last_name', 'part__name', 'part__assignment__description')