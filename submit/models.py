from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max


class Assignment(models.Model):
    description = models.CharField(max_length=10)
    due_date = models.DateField()

    def __unicode__(self):
        return self.description


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

    def save(self, *args, **kwargs):
        super(Submission, self).save(*args, **kwargs)

        try:
            part_grade = self.part.partgrade_set.all().filter(user=self.owner)[0]
            part_grade.get_current_score()
            part_grade.save()
        except IndexError:
            part_grade = PartGrade()
            part_grade.user = self.owner
            part_grade.part = self.part
            part_grade.current_score = self.awarded_points
            part_grade.save()

        try:
            assignment_grade = AssignmentGrade.objects.get(assignment=self.part.assignment, user=self.owner)
            assignment_grade.get_grade()
            assignment_grade.save()
        except AssignmentGrade.DoesNotExist:
            assignment_grade = AssignmentGrade()
            assignment_grade.assignment = self.part.assignment
            assignment_grade.user = self.owner
            assignment_grade.get_grade()
            assignment_grade.save()


class Line(models.Model):
    submission = models.ForeignKey(Submission)
    line_number = models.IntegerField()
    line = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.line


class PartGrade(models.Model):
    user = models.ForeignKey(User)
    part = models.ForeignKey(Part)
    current_score = models.IntegerField()

    def __unicode__(self):
        return "{0}".format(self.current_score)

    def get_current_score(self):
        submission = Submission.objects.filter(part=self, owner=self.user).order_by('-awarded_points')[0]
        current_score = submission.awarded_points
        self.current_score = current_score
        return self.current_score


class AssignmentGrade(models.Model):
    assignment = models.ForeignKey(Assignment)
    user = models.ForeignKey(User)
    grade = models.IntegerField()

    def __unicode__(self):
        return "{0}".format(self.grade)

    def get_parts(self):
        return self.assignment.part_set.all()

    def get_grade(self):
        parts = self.get_parts()
        grades = []
        grades_by_part_list = []
        for part in parts:
            grades_by_part_dict = {}
            part_grades = part.partgrade_set.all().filter(user=self.user)
            max_grade = part_grades.aggregate(Max('current_score'))['current_score__max']
            height_part_grade = part_grades.filter(current_score=max_grade).first()
            current_score = height_part_grade.current_score if height_part_grade else 0
            grades_by_part_dict['name'] = part.name
            grades_by_part_dict['score'] = current_score
            grades_by_part_list.append(grades_by_part_dict)
            grades.append(current_score)
        total_possible_points = [part.weight for part in parts]
        self.grade = int((sum(grades)/float(sum(total_possible_points))) * 100)
        return self.grade, grades_by_part_list