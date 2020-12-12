# serializers.py
from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('email',
                'first_name',
                'last_name',
                'hire_date',
                'termination_date',
                'employee_type',
                'division',
                'job_level',
                'location',
                'gender',
                'salary',
                'bonus',
                'shares',
                'restaurant',)


