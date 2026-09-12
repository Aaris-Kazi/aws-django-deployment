from django.db.models import QuerySet

class QuerySetModels(QuerySet):
    def get_subject_by_name(self, name: str) -> QuerySet:
        return self.get(name=name)
    
    def get_student_by_name(self, name: str) -> QuerySet:
        return self.get(name=name)
