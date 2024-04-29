from rest_framework import viewsets, mixins
from departments import models, serializers

class DepartmentView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = models.Department.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RetrieveDepartmentSerializer
        elif self.action == 'create':
            return serializers.DepartmentSerializer
        return serializers.DepartmentSerializer
    
class EmployeeView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = models.Employee.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RetrieveEmployeeSerializer
        elif self.action == 'create':
            return serializers.EmployeeSerializer
        return serializers.EmployeeSerializer
