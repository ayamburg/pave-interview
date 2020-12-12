# views.py
from rest_framework import viewsets

from .serializers import EmployeeSerializer
from .models import Employee


class EmplyeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('email')
    filter_fields = ('restaurant',)
    serializer_class = EmployeeSerializer
