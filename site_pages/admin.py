from django.contrib import admin
from .models import Customer_request
from django.contrib.auth.models import Group

@admin.register(Customer_request)
class Customer_requestAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'phone', 'status', 'created')
    list_filter = ('created', 'status')
    search_fields = ('name', 'surname', 'patronymic', 'phone')


admin.site.unregister(Group)
