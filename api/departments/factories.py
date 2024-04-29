import factory
from departments.models import Department


class DepartmentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Department