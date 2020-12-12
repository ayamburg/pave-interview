from django.core.management.base import BaseCommand, CommandError
from rgsf_database.models import Employee
import requests


api_url = 'https://api.airtable.com/v0/appX42ISdho4vdwsV/'

class Command(BaseCommand):

    def handle(self, *args, **options):
        employees = requests.get(api_url + 'Employees',
            headers={"Authorization": "Bearer keyw9eMTC6oHYMQcJ"},
            ).json()['records']

        salaries = requests.get(api_url + 'Salary',
            headers={"Authorization": "Bearer keyw9eMTC6oHYMQcJ"},
            ).json()['records']

        bonuses = requests.get(api_url + 'Bonus',
            headers={"Authorization": "Bearer keyw9eMTC6oHYMQcJ"},
            ).json()['records']

        sharess = requests.get(api_url + 'Shares',
            headers={"Authorization": "Bearer keyw9eMTC6oHYMQcJ"},
            ).json()['records']

        for employee in employees:
            fields = employee['fields']
            for salary in salaries:
                if fields['Email'] == salary['fields']['Email']:
                    fields['Salary'] = salary['fields']['Salary']
                    break
                fields['Salary'] = 0
            for bonus in bonuses:
                if fields['Email'] == bonus['fields']['Email']:
                    fields['Bonus'] = bonus['fields']['Bonus']
                    break
                fields['Bonus'] = 0
            for shares in sharess:
                if fields['Email'] == shares['fields']['Email']:
                    fields['Shares'] = float(shares['fields']['Shares'])
                    break
                fields['Shares'] = 0



            print(fields)

            employee = Employee(
                restaurant = 'Nabe',
                email = fields['Email'],
                first_name = fields['First name'],
                last_name = fields['Last name'],
                hire_date = fields['Hire date'],
                employee_type = fields['Employee type'],
                division = fields['Division'],
                job_level = fields['Job Level'],
                location = fields['Location'],
                gender = fields['Gender'],
                salary = fields['Salary'],
                bonus = fields['Bonus'],
                shares = fields['Shares']
            )
            employee.save()
