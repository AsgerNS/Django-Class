from rest_framework import serializers
from .models import Class, Student, Subject, Grade


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'year']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'classes', 'age', 'subjects']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'student', 'subject', 'grade']
