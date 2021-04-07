from . import views
from django.urls import path
urlpatterns = [
    path('main_page', views.index,name="main_page"),
    path("log",views.login_user),
    path("do_log",views.do_logout),
    path("do_register",views.register),
    path("course",views.course_start,name="course"),
    path("teachers",views.teachers_start,name="teachers"),
    path("achievements",views.achievements_start,name="achievements"),
    path("contacts",views.contacts_start,name="contacts"),
    path("timetable",views.timetable_start,name="timetable"),
    path("cheak_login",views.ajax_path),
    path("set_lang",views.translate),
    path("get_csv",views.get_csv),

]