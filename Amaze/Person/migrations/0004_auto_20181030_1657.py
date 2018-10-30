# Generated by Django 2.1.2 on 2018-10-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0003_auto_20181030_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.EmailField(max_length=50, verbose_name='课程名称')),
                ('descrption', models.TextField(verbose_name='课程描述')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, verbose_name='电子邮箱')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='modifydate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
        ),
    ]