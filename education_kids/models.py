from django.db import models


class Main(models.Model):
    name_main = models.CharField("Название", max_length=100)
    description_main = models.TextField("Описание курса")
    video_main = models.FileField("Видео")
    photo_1 = models.ImageField("Рисунок(1)")
    photo_2 = models.ImageField("Рисунок(2)")
    photo_3 = models.ImageField("Рисунок(3)")
    photo_4 = models.ImageField("Рисунок(4)")
    def __str__(self):
        return self.name_main
class Course(models.Model):
    name_course = models.CharField("Название курса",max_length=100)
    price_course = models.IntegerField("Стоимость курса",default=0)
    photo_1 = models.ImageField("Рисунок(1)")
    photo_2 = models.ImageField("Рисунок(2)")
    photo_3 = models.ImageField("Рисунок(3)")
    description = models.TextField("Описание курса")
    video = models.FileField("Видео")
    def __str__(self):
        return self.name_course
class Pupil(models.Model):
    name = models.CharField("Имя ученика",max_length=100)
    surname = models.CharField("Фамилия ученика",max_length=100)
    profile = models.CharField("Работы ученика",max_length=100)
    surname_teacher = models.CharField("Фамилия преподавателя",max_length=100)
    photo_1 = models.ImageField("Рисунок(1)")
    def __str__(self):
        return self.surname
class Teacher(models.Model):
    name = models.CharField("Имя преподавателя",max_length=100)
    surname = models.CharField("Фамилия преподавателя",max_length=100)
    education_level = models.CharField("Преподаваемые дисциплины",max_length=100)
    description = models.TextField("Информация о преподавателе")
    photo_1 = models.ImageField("Рисунок(1)")
    def __str__(self):
        return self.surname
class Achievements(models.Model):
    description = models.CharField("Информация о достижениях",max_length=100)
    photo_1 = models.ImageField("Рисунок(1)")
    photo_2 = models.ImageField("Рисунок(2)")
    photo_3 = models.ImageField("Рисунок(3)")
    photo_4 = models.ImageField("Рисунок(4)")
    photo_5 = models.ImageField("Рисунок(5)")
    photo_6 = models.ImageField("Рисунок(6)")
    def __str__(self):
        return self.description
class Payments(models.Model):
    name_of_course = models.ForeignKey(Course,verbose_name= "Название курса", on_delete = models.SET_NULL, null = True)
    surname_of_student = models.ForeignKey(Pupil,verbose_name= "Фамилия ученика", on_delete = models.SET_NULL, null = True)
    summa_of_payments = models.IntegerField("Сумма к оплате, €",default=0)
    count_of_courses = models.IntegerField("Количество занятий",default=0)
    def __str__(self):
        return self.surname_of_student.surname