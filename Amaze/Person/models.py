from django.db import models

# Create your models here.
class Person(models.Model):
    email=models.EmailField(verbose_name='电子邮箱',max_length=30)
    mobilephone=models.CharField(verbose_name='手机',max_length=11)
    username=models.CharField(verbose_name='姓名',max_length=10)
    age=models.IntegerField(verbose_name='年龄')
    password=models.CharField(verbose_name='密码',max_length=10)
    createdate=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    modifydate=models.DateTimeField(verbose_name='修改时间',auto_now_add=True)

class Teacher(models.Model):
    email=models.EmailField(verbose_name='电子邮箱',max_length=30)
    mobilephone = models.CharField(verbose_name='手机', max_length=11)
    username=models.CharField(verbose_name='姓名',max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    password = models.CharField(verbose_name='密码', max_length=10)
    createdate = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    modifydate = models.DateTimeField(verbose_name='修改时间', auto_now=True)

class Course(models.Model):
    name=models.EmailField(verbose_name='课程名称',max_length=50)
    descrption=models.TextField(verbose_name='课程描述',max_length=1000)
    createby=models.CharField(verbose_name='创建人', max_length=10)
    createdate = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    modifyby = models.CharField(verbose_name='修改人', max_length=10)
    modifydate = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    teachers=models.ManyToManyField("Teacher")