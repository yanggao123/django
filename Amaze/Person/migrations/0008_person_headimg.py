# Generated by Django 2.1.2 on 2018-10-31 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0007_course_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='headimg',
            field=models.ImageField(default='', upload_to='headimg', verbose_name='头像'),
            preserve_default=False,
        ),
    ]