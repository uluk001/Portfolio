# from distutils.command.upload import upload
# import email
# from email import message
# from tokenize import blank_re
# from turtle import title
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)



class Home_work(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.EmailField()
    gender = models.TextField()
    profession = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


class skill(models.Model):
    title = models.CharField(max_length=50, verbose_name ='Заголовок')
    discription = models.TextField(verbose_name='Описание')
    link = models.TextField(verbose_name='Ссылка')
    photo = models.ImageField(upload_to='main', blank=True, null=True, verbose_name='Изображение')
    sent_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата и время публикации')


class My_skill(models.Model):
    discription2 = models.TextField(verbose_name='Навыки')
    sent_at2 = models.DateTimeField(auto_now_add=True,verbose_name="Дата и время публикации")
