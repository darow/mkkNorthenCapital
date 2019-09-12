# Generated by Django 2.2.5 on 2019-09-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('amount_of_money', models.IntegerField(verbose_name='Сумма денег')),
                ('loan_term', models.IntegerField(verbose_name='Срок выдачи (дней)')),
            ],
            options={
                'verbose_name_plural': 'Заявки клиентов',
            },
        ),
    ]
