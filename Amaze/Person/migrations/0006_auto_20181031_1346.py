# Generated by Django 2.1.2 on 2018-10-31 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0005_auto_20181030_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='createby',
            field=models.CharField(default='', max_length=10, verbose_name='创建人'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='createdate',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='course',
            name='modifyby',
            field=models.CharField(default='', max_length=10, verbose_name='修改人'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='modifydate',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='createdate',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='mobilephone',
            field=models.CharField(default='', max_length=11, verbose_name='手机'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='modifydate',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default='', max_length=10, verbose_name='密码'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(default='', max_length=10, verbose_name='姓名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='descrption',
            field=models.TextField(max_length=1000, verbose_name='课程描述'),
        ),
    ]
