from django.shortcuts import render
from API.views import loginPageCheck, only
from API.database import fetchAdmission, fetchFoodItems,getAvailableRooms, fetchGrieveance

# Create your views here.

@loginPageCheck
def index(request):
    return render(request,"index.html")

@only('admin')
def admin(request):
    return render(request,"body/admin_crm.html")

@only('admin')
def admission_details(request):
    data=fetchAdmission()
    rooms = getAvailableRooms()
    return render(request, "body/admin_admission_body.html",{'data':data,'rooms':rooms})

@only('admin')
def food_body(request):
    data=fetchFoodItems()
    return render(request,"body/admin_food_body.html",{'fooditem':data})

@only('admin')
def accomodation_body(request):
    return render(request,"body/admin_accomodation_body.html")

@only('admin')
def student_details_body(request):
    
    return render(request,"body/admin_student_details_body.html")

@only('admin')
def grieveance_body(request):
    new_data = fetchGrieveance('new')
    old_data = fetchGrieveance('old')
    
    return render(request,"body/admin_grieveance_body.html",{'new':new_data, 'old':old_data})

def admission(request):
    return render(request, "admission.html")

@only('student')
def student(request):
    return render(request, "body/student_profile.html")

@only('student')
def student_food(request):
    return render(request, "body/student_food.html")

@only('student')
def student_grieveance(request):
    return render(request, "body/student_grieveance.html")

@only('student')
def student_remarks(request):
    return render(request, "body/student_remarks.html")


