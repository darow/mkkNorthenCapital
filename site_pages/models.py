from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomerRequest(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=30, verbose_name="Отчество")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    amount_of_money = models.IntegerField(verbose_name="Сумма денег")
    loan_term = models.IntegerField(verbose_name="Срок выдачи (дней)")
    status = models.CharField(max_length=30, verbose_name="Статус", default="Ожидает рассмотрения")
    created = models.DateTimeField( verbose_name="Время создания", default=timezone.now())

    def __str__(self):
        return self.name + self.surname + self.patronymic

    def body_preview(self):
        return self.phone

    class Meta:
        verbose_name_plural = 'Заявки клиентов'


class MyUserManager(BaseUserManager):
    def create_user(self, phone, name, surname, patronymic, amount_of_money=None, loan_term=None,  password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an email address')

        user = self.model(
            phone=phone,
            name=name[0].upper() + name[1:].lower(),
            surname=surname[0].upper() + surname[1:].lower(),
            patronymic=patronymic[0].upper() + patronymic[1:].lower(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    phone = models.CharField(max_length=12, verbose_name="Телефон", unique=True)
    name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=30, verbose_name="Отчество")
    status = models.CharField(max_length=30, verbose_name="Статус", default="Ожидает рассмотрения")
    created = models.DateTimeField(verbose_name="Время создания", default=timezone.now())

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'surname', 'patronymic']

    def __str__(self):
        return self.name + self.surname + self.patronymic

    def body_preview(self):
        return self.phone

    class Meta:
        verbose_name_plural = 'Пользователи'




