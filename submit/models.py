from django.contrib.auth.models import User
from django.db import models


class Assignment(models.Model):
    description = models.CharField(max_length=10)
    due_date = models.DateField()

    def __unicode__(self):
        return self.description

    def grade(self, user):
        parts = Part.objects.filter(assignment=self)
        possible = 0.0
        awarded = 0.0

        for part in parts:
            submits = Submission.objects.filter(part=part, owner=user)

            if len(submits) > 0:
                awarded += submits[0].best_grade

            possible += part.weight

        return 100 * awarded / possible

    def part_grades(self, user):
        parts = Part.objects.filter(assignment=self)
        grades = []

        for part in parts:
            submits = Submission.objects.filter(part=part, owner=user)

            if len(submits) > 0:
                awarded = submits[0].best_grade
            else:
                awarded = 0

            grade_dict = {'name': part.name, 'awarded': awarded, 'possible': part.weight}

            grades.append(grade_dict)

        return grades


class TestRunner(models.Model):
    script = models.CharField(max_length=1024)


class Part(models.Model):
    assignment = models.ForeignKey(Assignment)
    name = models.CharField(max_length=1024)
    tester = models.ForeignKey(TestRunner)
    test_script = models.CharField(max_length=1024)
    extra_files = models.CharField(max_length=1024)
    submit_filename = models.CharField(max_length=1024)
    output_file = models.CharField(max_length=1024)
    expected_result = models.CharField(max_length=1024)
    weight = models.IntegerField()
    order = models.IntegerField()

    def __unicode__(self):
        return self.name


class Submission(models.Model):
    owner = models.ForeignKey(User)
    submission_date = models.DateTimeField()
    part = models.ForeignKey(Part)
    test_results = models.CharField(max_length=1024, null=True, blank=True)
    awarded_points = models.IntegerField()
    output = models.CharField(max_length=4096)

    def __unicode__(self):
        if self.test_results.rstrip() == self.part.expected_result:
            result = 'Pass'
        else:
            result = 'Please try again, %s' % self.test_results

        return '%s|%s|%s' % (self.owner.username, self.part.name, result)

    @property
    def best_grade(self):
        submits = Submission.objects.filter(part=self.part, owner=self.owner).order_by('-awarded_points')

        if len(submits) > 0:
            return submits[0].awarded_points
        else:
            return 0

    @property
    def assignment_grade(self):
        parts = Part.objects.filter(assignment=self.part.assignment)
        grade = 0

        for part in parts:
            grade += Submission.objects.filter(part=part)[0].best_grade


class Line(models.Model):
    submission = models.ForeignKey(Submission)
    line_number = models.IntegerField()
    line = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.line
