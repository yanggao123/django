# Generated by Django 2.1.2 on 2018-10-30 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, verbose_name='电子邮箱')),
                ('mobilephone', models.CharField(max_length=11, verbose_name='手机')),
                ('username', models.CharField(max_length=10, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('password', models.CharField(max_length=10, verbose_name='密码')),
            ],
        ),
    ]