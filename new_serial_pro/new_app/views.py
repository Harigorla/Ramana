from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeCrudCbv(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            seri = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(seri.data)
            return HttpResponse(json_data, content_type='json')
        qs = Employee.objects.all()
        seri = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(seri.data)
        return HttpResponse(json_data, content_type='json')
