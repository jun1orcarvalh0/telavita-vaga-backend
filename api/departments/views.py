from rest_framework import viewsets, mixins, status
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department_id']

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RetrieveEmployeeSerializer
        elif self.action == 'create':
            return serializers.EmployeeSerializer
        return serializers.EmployeeSerializer
    
    def get_queryset(self):
        department_id = self.request.query_params.get('department_id')
        if not department_id:
            content = {'detail': 'O parâmetro "department_id" é obrigatório para esta consulta.'}
            raise ValidationError(content, code=status.HTTP_400_BAD_REQUEST)

        return self.queryset.filter(department_id=department_id)
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('department_id', openapi.IN_QUERY, description="ID do Departamento", type=openapi.TYPE_INTEGER, required=True)
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)