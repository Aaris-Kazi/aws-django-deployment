from django.contrib import admin
from .models import Subject, Student
# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

    search_fields = [
        'name'
    ]

    ordering = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'subjects',
        'DOB',
        'age',
    ]

    search_fields = [
        'name',
        'subjects',
        'DOB',
        'age'
    ]

    ordering = ['name']
