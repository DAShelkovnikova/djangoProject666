# Generated by Django 5.1.2 on 2024-11-03 22:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ф.И.О')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('comment', models.TextField(blank=True, max_length=100, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_letter', models.CharField(max_length=100, verbose_name='Тема')),
                ('body_letter', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time_of_sending', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата и время первой отправки отправки')),
                ('periodicity', models.CharField(choices=[('Раз в день', 'Раз в день'), ('Раз в неделю', 'Раз в неделю'), ('Раз в месяц', 'Раз в месяц')], default='Раз в день', max_length=50, verbose_name='Периодичность рассылки')),
                ('status', models.CharField(choices=[('Завершена', 'Завершена'), ('Создана', 'Создана'), ('Запущена', 'Запущена')], default='Создана', max_length=50, verbose_name='Статус')),
                ('next_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время следующей отправки отправки')),
                ('clients', models.ManyToManyField(to='messages1.client', verbose_name='Клиенты')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='messages1.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ('id',),
                'permissions': [('can_edit_status', 'can_edit_status')],
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_last_attempt', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последнего попытки отправки')),
                ('status', models.CharField(choices=[('Успешно', 'Успешно'), ('Не успешно', 'Не успешно')], default='Не успешно', max_length=50, verbose_name='Статус попытки')),
                ('mail_server_response', models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='messages1.mailinglist', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Попытка',
                'verbose_name_plural': 'Попытки',
                'ordering': ('id',),
            },
        ),
    ]