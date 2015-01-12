from django.contrib.auth.models import User
from rest_framework import serializers
from submit.models import Assignment, AssignmentGrade,  Part, Line


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


class AssignmentGradeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    assignment = AssignmentSerializer()

    class Meta:
        model = AssignmentGrade
