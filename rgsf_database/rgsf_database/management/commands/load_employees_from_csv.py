import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from rgsf_database.models import Employee
import requests


api_url = 'https://api.airtable.com/v0/appX42ISdho4vdwsV/'

class Command(BaseCommand):

    def handle(self, *args, **options):
        all_employees = []

        df = pd.read_csv('csvs/fogoDeChao.csv', delimiter=',')
        for index, row in df.iterrows():
            fields = {'Email': '', 'First name': '', 'Last name': '', 'Hire date': '', 'Employee type': '',
                      'Division': '', 'Job Level': 0, 'Location': '', 'Gender': '', 'Salary': 0, 'Bonus': 0,
                      'Shares': 0, 'Termination date': ''}
            fields['Email'] = row['Email']
            fields['First name'] = row['First Name']
            fields['Last name'] = row['Last Name']
            fields['Hire date'] = row['Hire Date']
            fields['Employee type'] = row['Type']
            fields['Division'] = row['Division']
            fields['Location'] = row['Country']
            fields['Gender'] = row['Gender']
            fields['Salary'] = row['Base Pay']
            fields['Bonus'] = row['Bonus']
            fields['Shares'] = row['Equity (Shares)']
            fields['Restaurant'] = 'fogoDeChao'
            all_employees += [fields]

        df = pd.read_csv('csvs/gamine.csv', delimiter=',')
        for index, row in df.iterrows():
            fields = {'Email': '', 'First name': '', 'Last name': '', 'Hire date': '', 'Employee type': '',
                      'Division': '', 'Job Level': 0, 'Location': '', 'Gender': '', 'Salary': 0, 'Bonus': 0,
                      'Shares': 0, 'Termination date': ''}
            fields['Email'] = row['email']
            fields['First name'] = row['firstName']
            fields['Last name'] = row['lastName']
            fields['Hire date'] = row['startDate']
            fields['Termination date'] = row['terminationDate']
            fields['Employee type'] = row['employmentType']
            fields['Division'] = row['department']
            fields['Location'] = row['city'] + ', USA'
            fields['Gender'] = row['gender']
            fields['Job Level'] = row['level']
            fields['Salary'] = row['salary']
            fields['Bonus'] = row['bonus']
            fields['Restaurant'] = 'gamine'
            all_employees += [fields]

        df = pd.read_csv('csvs/hookfish.csv', delimiter=',')
        for index, row in df.iterrows():
            fields = {'Email': '', 'First name': '', 'Last name': '', 'Hire date': '', 'Employee type': '',
                      'Division': '', 'Job Level': 0, 'Location': '', 'Gender': '', 'Salary': 0, 'Bonus': 0,
                      'Shares': 0, 'Termination date': ''}
            fields['Email'] = row['email']
            fields['First name'] = row['firstName']
            fields['Last name'] = row['lastName']
            fields['Hire date'] = row['startDate']
            fields['Employee type'] = row['employmentType']
            fields['Division'] = row['department']
            fields['Location'] = row['city'] + ', USA'
            fields['Gender'] = row['gender']
            fields['Job Level'] = row['level']
            fields['Salary'] = row['salary']
            fields['Bonus'] = row['bonus']
            fields['Restaurant'] = 'hookfish'
            all_employees += [fields]

        df = pd.read_csv('csvs/zenYai.csv', delimiter=',')
        for index, row in df.iterrows():
            fields = {'Email': '', 'First name': '', 'Last name': '', 'Hire date': '', 'Employee type': '',
                      'Division': '', 'Job Level': 0, 'Location': '', 'Gender': '', 'Salary': 0, 'Bonus': 0,
                      'Shares': 0, 'Termination date': ''}
            fields['Email'] = row['email']
            fields['First name'] = row['firstName']
            fields['Last name'] = row['lastName']
            fields['Hire date'] = row['startDate']
            fields['Employee type'] = row['employmentType']
            fields['Division'] = row['department']
            fields['Location'] = row['city'] + ', USA'
            fields['Gender'] = row['gender']
            fields['Job Level'] = row['level']
            fields['Salary'] = row['salary']
            fields['Shares'] = row['shares']
            fields['Restaurant'] = 'zenYai'
            all_employees += [fields]

        print(all_employees)

        for fields in all_employees:
            employee = Employee(
                restaurant = fields['Restaurant'],
                email = fields['Email'],
                first_name = fields['First name'],
                last_name = fields['Last name'],
                hire_date = fields['Hire date'],
                termination_date = fields['Termination date'],
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



