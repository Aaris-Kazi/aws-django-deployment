# from django.db import models

from django.db.models import Model, CharField, ForeignKey, CASCADE, DateField, IntegerField, Index
from django.core.validators import MaxValueValidator
from django.utils import timezone
from .QuerySetsModels import QuerySetModels
# Create your models here.


class Subject(Model):
    name = CharField(blank=False, max_length=30)
    manager = QuerySetModels.as_manager()
    

    class Meta:
        db_table = "subject"
        indexes = [
            Index(fields=["name"]),
        ]
        unique_together = ("name",)


    def __str__(self) -> str:
        return self.name


class Student(Model):
    name = CharField(blank=False, max_length=150, unique=True)
    subjects = ForeignKey(
        Subject,
        on_delete = CASCADE,
        null=True,
        related_name="students"
    )
    DOB = DateField(default=timezone.now)
    age = IntegerField(default=0, validators=[MaxValueValidator(10)])
    objects = QuerySetModels.as_manager()
    class Meta:
        db_table = "student"
        indexes = [
            Index(fields=["name"]),
        ]
        unique_together = ("name",)

    def __str__(self) -> str:
        return self.name
