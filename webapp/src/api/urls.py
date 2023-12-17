from django.urls import path
from . import views

urlpatterns = [
    # Реализация REST API для управления книгами и добавления пользователей

    path('items/', views.BooksList.as_view(), name='item-list'),
    path('items/<int:pk>/', views.BooksDetail.as_view(), name='item-detail'),
    path('users/', views.UsersList.as_view(), name='add-user'),
]