from django.contrib import admin
from .models import Books, Users


# ---------- Настройка Панели администратора ----------
class BooksAdmin(admin.ModelAdmin):
    search_fields = ['name', 'author', 'year', 'isbn']
    list_display = ['isbn', 'author', 'name', 'year']
    list_filter = ['author', 'year']


class UsersAdmin(admin.ModelAdmin):
    search_fields = ['date_register', 'name', 'email']
    list_display = ['email', 'date_register', 'name']
    list_filter = ['date_register']


# ---------- Регистрация Моделей ----------

admin.site.register(Books, BooksAdmin)
admin.site.register(Users, UsersAdmin)