from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request

from testApplication.serializers import StudentSerializer, SubjectSerializer, StudentSerializerResponse, SubjectSerializerResponse

from .services import Services

# Create your views here.

# services = Services()

@api_view(['GET'])
def health_check(request: Request):
    return JsonResponse({"status": "healthy"})


class Subject(ViewSet):
    def create(self, request: Request):
        data = SubjectSerializer(data=request.data)
        if not data.is_valid():
            return JsonResponse({"message": "Invalid data provided"}, status=400)
        data:dict = data.validated_data
        subject:str = Services.addingSubject(data.get("name"))
        
        return JsonResponse({"message": subject}, status=200)

    def list(self, request: Request):
        
        subjects = Services.getAllSubject()
        subjectSerializer = SubjectSerializerResponse(subjects, many=True)
        return JsonResponse({"message": subjectSerializer.data}, status=200)
    
    def retrieve(self, request: Request, pk: str):
        response = {}
        status = 200
        try:
            subject:str = Services.getSubject(pk)
            response.update({"message": subject})
        except Exception as e:
            status = 404
            response.update({"message": f"Subject not found {e}"})

        return JsonResponse(response, status=status)

class Student(ViewSet):
    def create(self, request:Request):
        studentSerializer = StudentSerializer(data=request.data)
        if studentSerializer.is_valid():
            Services.addStudent(studentSerializer)
            return JsonResponse({"message": "Student created successfully"}, status=201)
        return JsonResponse({"message": "Invalid data provided"}, status=400)
    
    def retrieve(self, request: Request, pk: str):

        try:
            student = Services.getStudent(pk)
            studentSerializer = StudentSerializerResponse(student)
            return JsonResponse({"message": studentSerializer.data}, status=200)
        except Exception as e:
            return JsonResponse({"message": f"Student not found {e}"}, status=404)
        