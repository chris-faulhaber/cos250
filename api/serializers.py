from django.contrib.auth.models import User
from rest_framework import serializers
from submit.models import Assignment, Part, Line
from django.db import models


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class PartSerializer(serializers.ModelSerializer):
    grade = serializers.IntegerField()
    lines = LineSerializer(many=True)

    class Meta:
        model = Part


class AssignmentGrade(models.Model):
    assignment = models.ForeignKey(Assignment)
    user = models.ForeignKey(User)
    grade = models.IntegerField()


class AssignmentGradeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    assignment = AssignmentSerializer()
    grade = serializers.IntegerField()

    class Meta:
        model = AssignmentGrade


class PartGrade(models.Model):
    assignment = models.ForeignKey(Assignment)
    user = models.ForeignKey(User)
    grade = models.IntegerField()


class PartGradeSerializer(serializers.ModelSerializer):
    user = models.ForeignKey(User)
    part = models.ForeignKey(Part)
    current_score = models.IntegerField()

    class Meta:
        model = PartGrade