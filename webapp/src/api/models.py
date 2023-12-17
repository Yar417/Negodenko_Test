from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator as MaxVV
from django.core.validators import MinValueValidator as MinVV
from django.dispatch import receiver
from django.db.models.signals import post_save
from . import tasks

# ---------- Книги ----------

class Books(models.Model):
    name = models.CharField('Name', max_length=200, null=False)
    author = models.CharField('Author', max_length=200, null=True, blank=True)
    year = models.IntegerField('The year of publishing',
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


@receiver(post_save, sender=Users)
def user_created(sender, instance, created, **kwargs):
    '''
    При регистрации новых пользователей через API
    просходит ансинхронная отправка электронной почты
    на адрес нового пользователя, как того требует задание.
    '''
    if created:
        tasks.send_mail_new_user.delay(instance.email)

'''
Готово!
Используя механизм ветвления в Git, создайте 
отдельную ветку для исправления ошибки в коде вашего приложения. 
Назовите ветку, например, bugfix/registration. 
'''