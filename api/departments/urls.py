from django.urls import path, include
from departments import views
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register('', views.DepartmentView, basename='department')
router.register('employees', views.EmployeeView, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]