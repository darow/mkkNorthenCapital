from django.db import models


class Customer_request(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=30, verbose_name="Отчество")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    amount_of_money = models.IntegerField(verbose_name="Сумма денег")
    loan_term = models.IntegerField(verbose_name="Срок выдачи (дней)")
    status = models.CharField(max_length=30, verbose_name="Статус", default="Ожидает рассмотрения")

    class Meta:
        verbose_name_plural = 'Заявки клиентов'


