from django.contrib import admin
from .models import CustomerRequest, MyUser
from django.contrib.auth.models import Group


@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'phone', 'status', 'created')
    list_filter = ('created', 'status')
    search_fields = ('name', 'surname', 'patronymic', 'phone')
    readonly_fields = ('created',)


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'phone', 'status', 'created')
    list_filter = ('created', 'status')
    search_fields = ('name', 'surname', 'patronymic', 'phone')
    readonly_fields = ('created',)

admin.site.unregister(Group)
