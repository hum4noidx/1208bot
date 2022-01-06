# Generated by Django 4.0 on 2022-01-04 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lsn_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('uses', models.IntegerField()),
                ('user_class', models.IntegerField()),
                ('user_prof', models.CharField(max_length=10)),
                ('user_math', models.CharField(max_length=10)),
                ('vip', models.BooleanField()),
                ('admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('specialization', models.CharField(max_length=200, verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lsn_number', models.IntegerField(
                    choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
                             (9, '9')])),
                ('lsn_class', models.CharField(max_length=15, verbose_name='Кабинет')),
                ('lsn_date', models.IntegerField(
                    choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница')],
                    verbose_name='День недели')),
                ('lsn_grade',
                 models.IntegerField(choices=[(5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11')],
                                     verbose_name='Класс')),
                ('lsn_profile', models.CharField(
                    choices=[('fm', 'Физмат'), ('gum', 'Гуманитарий'), ('se', 'Соцэконом'), ('bh', 'Биохим'),
                             ('med', 'Медицинский'), ('media', 'Медиа'), ('akadem', 'Академический'),
                             ('it', 'It/Инженеры')], max_length=200, verbose_name='Профиль')),
                ('lsn_math',
                 models.CharField(choices=[('prof', 'Профильная'), ('base', 'Базовая'), ('None', 'Нет математики')],
                                  max_length=15, verbose_name='Математика')),
                ('lsn_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.discipline')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
            options={
                'verbose_name': 'График',
                'verbose_name_plural': 'Графики',
            },
        ),
    ]
