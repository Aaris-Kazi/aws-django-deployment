from rest_framework.serializers import Serializer, CharField

class SubjectSerializer(Serializer):
    name = CharField(max_length=100)