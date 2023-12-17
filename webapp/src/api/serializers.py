from rest_framework import serializers
from .models import Books, Users
import datetime


# Serializer для API

class BooksSerializer(serializers.ModelSerializer):
    '''
    Добавил валидатор даты издания книги
    '''
    def validate_year(self, year):
        if year > datetime.date.today().year:
            raise serializers.ValidationError("Год издания не может быть больше текущего года.")
        return year

    '''
    def validate_isbn(self, value):
        # Здесь можно добавить проверку формата ISBN
        return value
    '''

    class Meta:
        model = Books
        fields = '__all__'

# Serializer для Users
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
