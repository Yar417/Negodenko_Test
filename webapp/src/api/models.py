from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator as MaxVV
from django.core.validators import MinValueValidator as MinVV


# ---------- Книги ----------

class Books(models.Model):
    name = models.CharField('Name', max_length=200, null=False)
    author = models.CharField('Author', max_length=200, null=True, blank=True)
    year = models.IntegerField('The year of publishing',
                               default=timezone.now,
                               validators=[MinVV(0), MaxVV(3000)]
                               )
    # С 1 января 2007 года введён новый стандарт ISBN — 13-значный, ранее состоял из 9-ти
    isbn = models.IntegerField('ISBN',
                               unique=True,
                               null=False,
                               validators=[MinVV(99999999), MaxVV(9999999999999)]
                               )

    def __str__(self):
        return f'{self.author}: {self.name} ({self.year})'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


# ---------- Пользователи ----------

class Users(models.Model):
    name = models.CharField("Username", max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'User №{self.id}: {self.name} ({self.date_register})'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'