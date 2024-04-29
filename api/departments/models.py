from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    dependents = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.full_name
