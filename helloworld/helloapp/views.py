from django.shortcuts import render
from django.http import HttpResponse
from .models import employeedetails
from django.views.generic.list import ListView 

# Create your views here.
def index(request):

   

    emp = employeedetails.objects.all()[:10]
    emp_list = []

    for e in emp:

        e_list = {

            'name' : e.name,
            'location':e.location,
            'designation':e.designation,
            'servicestart':e.servicestart,
            'serviceends':e.serviceends
        }

        emp_list.append(e_list)

    context = {
        'employee': emp_list
    }

    return render(request,'index.html',context)


# def details(request,id):
#     emp_l = employeedetails.objects.get(id=id)

#     context = {
#         'emp_l': emp_l
#         }

#     return render(request,'details.html',context)

# class emplist(ListView): 
  
#     # specify the model for list view 
#     model = employeedetails 

