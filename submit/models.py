from django.db import models


class Person(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Person)

    def __unicode__(self):
        return self.name


class Attendee(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Person)

    def __unicode__(self):
        return self.course.name + "/" + self.student.email


class Assignment(models.Model):
    description = models.CharField(max_length=10)
    due_date = models.DateField()
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.description


class Submission(models.Model):
    owner = models.ForeignKey(Person)
    submission_date = models.DateTimeField()
    assignment = models.ForeignKey(Assignment)
    test_results = models.CharField(max_length=1024, null=True, blank=True)

    def __unicode__(self):
        return '%s|%s' % (self.owner, self.assignment.description)


class Line(models.Model):
    submission = models.ForeignKey(Submission)
    line_number = models.IntegerField()
    line = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return self.line

