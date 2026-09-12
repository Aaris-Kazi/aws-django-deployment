
from rest_framework.serializers import ModelSerializer, StringRelatedField

from testApplication.models import Student, Subject


class SubjectSerializerResponse(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class StudentSerializerResponse(ModelSerializer):
    subjects = StringRelatedField()
    class Meta:
        model = Student
        fields = "__all__"