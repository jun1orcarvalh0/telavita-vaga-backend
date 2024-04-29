from rest_framework import serializers
from departments import models

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = [
            'id',
            'name'
            ]

class RetrieveDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = [
            'name'
            ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = [
            'id',
            'full_name',
            'department',
            'dependents'
            ]

class RetrieveEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = [
            'id',
            'full_name',
            'have_dependents'
            ]
        
    have_dependents = serializers.SerializerMethodField()

    def get_have_dependents(self, obj):
        if obj.dependents > 0:
            return True
        return False
