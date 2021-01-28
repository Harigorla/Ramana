from django.shortcuts import render
from django.http import HttpResponse


def emp_view(request):
    emp_data = {
        'eno': '101',
        'ename': 'Harinadha',
        'esal': '25000',
        'eaddr': 'Bng',
    }
    resp = 'Employee Number:{}Employee Name:{} Employee Salary:{} Employee Address:{}'.format(emp_data['eno'],
                                                                                              emp_data['ename'],
                                                                                              emp_data['esal'],
                                                                                              emp_data['eaddr'])
    return HttpResponse(resp)
