# Generated by Django 3.2a1 on 2021-04-03 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education_kids', '0016_auto_20210331_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa_of_payments', models.IntegerField(default=0, verbose_name='Сумма к оплате, €')),
                ('count_of_courses', models.IntegerField(default=0, verbose_name='Количество занятий')),
                ('name_of_course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education_kids.course', verbose_name='Название курса')),
                ('surname_of_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education_kids.pupil', verbose_name='Фамилия ученика')),
            ],
        ),
    ]