from django.db import models


class Person(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email


class Attendee(models.Model):
    student = models.ForeignKey(Person)

    def __unicode__(self):
        return self.student.email


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
    expected_result = models.CharField(max_length=1024)
    weight = models.IntegerField()

    def __unicode__(self):
        return self.name


class Submission(models.Model):
    owner = models.ForeignKey(Person)
    submission_date = models.DateTimeField()
    part = models.ForeignKey(Part)
    test_results = models.CharField(max_length=1024, null=True, blank=True)

    def __unicode__(self):
        if self.test_results.rstrip() == self.part.expected_result:
            result = 'Pass'
        else:
            result = 'Please try again, %s' % self.test_results

        return '%s|%s|%s' % (self.owner.email, self.part.name, result)


class Line(models.Model):
    submission = models.ForeignKey(Submission)
    line_number = models.IntegerField()
    line = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return self.line

