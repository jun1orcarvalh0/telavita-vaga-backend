from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from departments.factories import DepartmentFactory

class DepartmentTestCases(APITestCase):
    def setUp(self):
        self.url = '/core/departments'

    def test_create_department(self):
        response = self.client.post(self.url, {'name': 'HR'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'HR')

    def test_wont_create_department_when_name_is_not_sent(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'name': ['Este campo é obrigatório.']})

    def test_get_departments_list(self):
        DepartmentFactory.create(name="HR")
        DepartmentFactory.create(name="IT")

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{'name': 'HR'}, {'name': 'IT'}])

class EmployeeTestCases(APITestCase):
    def setUp(self):
        self.url = '/core/employees'
        self.department = DepartmentFactory(name="HR")

    def test_create_employee(self):
        response = self.client.post(self.url, {
            'full_name': 'Steve Jobs',
            'department': self.department.id,
            'dependents': 50
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], 'Steve Jobs')
        self.assertEqual(response.data['department'], self.department.id)
        self.assertEqual(response.data['dependents'], 50)
    
    def test_wont_create_employee_when_full_name_is_not_sent(self):
        response = self.client.post(self.url, {
            'department': self.department.id,
            'dependents': 20
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'full_name': ['Este campo é obrigatório.']})

    def test_wont_create_employee_when_department_is_not_sent(self):
        response = self.client.post(self.url, {
            'full_name': 'Steve Jobs',
            'dependents': 20
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'department': ['Este campo é obrigatório.']})

    def test_get_employees_by_department_id(self):
        self.client.post(self.url, {
            'full_name': 'Steve Jobs',
            'department': self.department.id,
            'dependents': 24
        })
        self.client.post(self.url, {
            'full_name': 'Lucas Montano',
            'department': self.department.id,
            'dependents': 0
        })

        response = self.client.get(f'{self.url}?department_id={self.department.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{'id': 2, 'full_name': 'Steve Jobs', 'have_dependents': True}, {'id': 3, 'full_name': 'Lucas Montano', 'have_dependents': False}])