import logging

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions

from submit.models import AssignmentGrade, Assignment

log = logging.getLogger(__name__)

from serializers import *


class AssignmentGradeView(APIView):
    serializer_class = AssignmentGradeSerializer

    def get_object(self, id):
        try:
            return Assignment.objects.get(id=id)
        except AssignmentGrade.DoesNotExist:
            raise Http404

    def get(self, request, id=None):
        try:
            assignment = self.get_object(id)
            grades = AssignmentGrade.objects.filter(assignment=assignment)
            serializer = self.serializer_class(grades, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            log.warning(ex)
            return Response(data="not found", status=status.HTTP_404_NOT_FOUND)


class PartGradeView(APIView):
    serializer_class = PartSerializer