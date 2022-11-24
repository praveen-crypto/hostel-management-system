from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

from API import database

import json
# Create your views here.

def only(name):
    def checking(func):
        def validate(args):
            if 'user' not in args.session:
                return redirect("/")
            email,usertype = args.session['user'].split("&&")
            if usertype != name:
                return redirect("/")
            if name != database.fetchUsertype(email):
                return redirect("/")
            return func(args)
        return validate
    return checking


def loginPageCheck(func):
    def validate(args):
        if 'user' in args.session:
            email,usertype = args.session['user'].split("&&")
            value = database.fetchUsertype(email)
            if value==usertype:
                return redirect("/"+value)
            else:
                args.session['user'] = "null&&null"
        return func(args)
    return validate


def check(request):
    try:
        if request.method != "POST":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        userType = database.checkUser(email,pwd)
        if userType==None:
            return JsonResponse({'type':"null",'message': 'Bad Request'}, status = 200)
        request.session['user'] = email+"&&"+userType
        
        return JsonResponse({'type': userType,'message': 'ok'}, status = 200)
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'server error'}, status = 500)

def logout(request):
    try:
        request.session['user'] = "null&&null"
        return redirect("/")
        
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'server error'}, status = 500)

def insertStudent(request):
    try:
        if request.method != "POST":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        data = request.POST.get("data")
        print("data =", data)
        data = json.loads(data)
        print(type(data), data  )
        if(database.addStudent(data)):
            return JsonResponse({'message': 'ok'}, status = 200)
        else:
            return JsonResponse({'message': 'failed'}, status = 200)
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'server error'}, status = 500)

def newApplications(request):
    try:
        return JsonResponse({'message': 'ok','data':database.fetchAdmission()}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

@csrf_exempt
def getStudentDetails(request):
    try:
        if request.method != "GET":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        email,usertype = request.session['user'].split("&&")
        if email=="admin":
            data = database.getStudent()
        else:
            data = database.getStudent(email)
        print(data)
        return JsonResponse({'message': 'ok','data':data}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

def setApprove(request):
    try:
        if request.method != "POST":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        email = request.POST.get("email")
        rooms_id = request.POST.get("rooms_id")
        data = database.setApprove(email,rooms_id)
        if(data):
            return JsonResponse({'message': 'ok'}, status = 200)
        else:
            return JsonResponse({'message': 'failed'}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

def getRoomsDetails(request):
    try:
        if request.method != "GET":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        data = database.getRoomsDetails()
        return JsonResponse({'message': 'ok','data':data}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

def getAvailableRooms(request):
    try:
        if request.method != "GET":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        data = database.getAvailableRooms()
        return JsonResponse({'message': 'ok','data':data}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

def addMenuItem(request):
    try:
        if request.method != "POST":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        item = request.POST.get("item")
        data = database.addMenuItem(item)
        if(data):
            return JsonResponse({'message': 'ok'}, status = 200)
        else:
            return JsonResponse({'message': 'failed'}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)


def fetchFoodItems(request):
    try:
        if request.method != "GET":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        data = database.fetchFoodItems()
        return JsonResponse({'message': 'ok','data':data}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)


def addDailyItem(request):
    try:
        if request.method != "POST":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        date = request.POST.get("date")
        breakfast = request.POST.get("breakfast")
        lunch = request.POST.get("lunch")
        dinner = request.POST.get("dinner")
        data = database.addDailyItem(date,breakfast,lunch,dinner)
        if(data):
            return JsonResponse({'message': 'ok'}, status = 200)
        else:
            return JsonResponse({'message': 'failed'}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

def FetchDailyItem(request):
    try:
        if request.method != "POST":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        date = request.POST.get("date")
        data = database.FetchDailyItem(date)
        return JsonResponse({'message': 'ok','data':data}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

def fetchGrieveance(request):
    try:
        if request.method != "GET":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        typ = request.GET.get("type")
        data = database.fetchGrieveance(typ)
        return JsonResponse({'message': 'ok','data':data}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

def setGrieveanceViewed(request):
    try:
        if request.method != "POST":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        id = request.POST.get("id")
        data = database.setGrieveanceViewed(id)
        if(data):
            return JsonResponse({'message': 'ok'}, status = 200)
        else:
            return JsonResponse({'message': 'failed'}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)

def newGrieveance(request):
    try:
        if request.method != "POST":
            return JsonResponse({'message': 'Bad Request'}, status = 400)
        title = request.POST.get("title")
        body = request.POST.get("body")
        email,usertype = request.session['user'].split("&&")
        data = database.newGrieveance(title,body,email)
        if(data):
            return JsonResponse({'message': 'ok'}, status = 200)
        else:
            return JsonResponse({'message': 'failed'}, status = 200)
    except:
        return JsonResponse({'message': 'server error'}, status = 500)