from testApplication.serializers import StudentSerializer

from .models import Subject, Student
from datetime import date

class Services:

    @staticmethod
    def calculateAge(dob: date) -> int:
        today = date.today()
        # return today.year - dob.year - (today.month, today.day) < (dob.month, dob.day)
        return today.year - dob.year

    @staticmethod
    def addingSubject(sub_name: str) -> str:

        subjectModel, created = Subject.objects.get_or_create(name=sub_name)
        if not created:
            subjectModel.name = sub_name
            subjectModel.save()
        return sub_name
    
    @staticmethod
    def getSubject(sub_name: str) -> str:
        subjectModel = Subject.manager.get_subject_by_name(sub_name)
        return subjectModel.name
    
    @staticmethod
    def getAllSubject() -> Subject:

        return Subject.objects.all()

    @staticmethod
    def addStudent(student: StudentSerializer) -> None:
        data:dict = student.validated_data
        Student.objects.update_or_create(
            name=data.get("name"),
            defaults={
                "DOB": data.get("dob"),
                "age": Services.calculateAge(data.get("dob")),
                "subjects": Subject.objects.get(name=data.get("subject")),
            },
        )

    @staticmethod
    def getStudent(name: str) -> Student:
        return Student.objects.select_related("subjects").get(name=name)
