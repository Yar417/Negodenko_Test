from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.BooksList.as_view(), name='item-list'),
    path('items/<int:pk>/', views.BooksDetail.as_view(), name='item-detail'),
    path('users/', views.UsersList.as_view(), name='add-user'),
]