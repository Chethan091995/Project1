from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Employ,Position
from . forms import EmployeeForm
# Create your views here.

def employee_list(request):
    context={'employee_list':Employ.objects.all()}
    return render(request,"myapp/employee_list.html",context)

def employee_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee=Employ.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"myapp/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employ.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)

        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Employeelist")

def employee_delete(request,id):
    employee = Employ.objects.get(pk=id)
    employee.delete()
    return redirect("Employeelist")

    