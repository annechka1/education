from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from education_kids.models import *
from django.utils.translation import activate
from django.conf import settings
from django.http import HttpResponse
import csv


def index(request):
    main = Main.objects.filter(id=1)
    return render(request, "index.html",{"main_list":main})

def translate(request):
    activate(request.GET["code"])
    response = HttpResponseRedirect("/main_page")
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME,request.GET["code"],
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    return response

def course_start(request):
    course = Course.objects.filter(id=1)
    course_1 = Course.objects.filter(id=2)
    course_2 = Course.objects.filter(id=3)
    course_3 = Course.objects.filter(id=4)
    return render(request, "course.html", {"course_list":course,"course_list_2":course_1,"course_list_3":course_2,"course_list_4":course_3})
def teachers_start(request):
    teachers = Teacher.objects.filter(id=1)
    teachers_2 = Teacher.objects.filter(id=3)
    teachers_3 = Teacher.objects.filter(id=4)
    teachers_4 = Teacher.objects.filter(id=5)
    return render(request, "teachers.html", {"teachers_list": teachers,"teachers_list_2": teachers_2,"teachers_list_3": teachers_3,"teachers_list_4": teachers_4})
def achievements_start(request):
    achievements = Achievements.objects.filter(id=1)
    return render(request,"achievements.html",{"achievements_list":achievements})
def contacts_start(request):
    return render(request,"contacts.html")
def timetable_start(request):
    course = Course.objects.filter(id=1)
    course_1 = Course.objects.filter(id=2)
    course_2 = Course.objects.filter(id=3)
    course_3 = Course.objects.filter(id=4)
    return render(request,"timetable.html",{"course_list":course,"course_list_2":course_1,"course_list_3":course_2,"course_list_4":course_3})

def login_user(request):
    user=authenticate(
        username=request.POST["username"],
        password=request.POST["password"]
    )
    if user is None:
        return render(request,"index.html",{"some_information": "Пользователь не существует"})
    else:
        login(request,user)
        return HttpResponseRedirect("/main_page")
def ajax_path(request):
    users = User.objects.filter(username=request.POST["login"])
    if len(users) != 0:
        response = {
           "exist": 1
        }
    else:
        response = {
           "exist": 0
        }
    return JsonResponse(response)


def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/main_page")

def register(request):
    user=User.objects.create_user(
        username=request.POST["username"],
        password=request.POST["password"]
    )
    return HttpResponseRedirect("/main_page")

def get_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] ="attachment; filename = Payments.csv"

    writer = csv.writer(response)
    writer.writerow(['id','summa_of_payments','count_of_courses','name_of_course','surname_of_student'])
    payments = Payments.objects.all()
    for payment in payments:
        writer.writerow([payment.id,payment.summa_of_payments,payment.count_of_courses,payment.name_of_course,payment.surname_of_student])
    return response
# Create your views here.


