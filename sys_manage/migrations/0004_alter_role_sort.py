# Generated by Django 4.1 on 2022-08-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_manage', '0003_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='sort',
            field=models.IntegerField(null=True, verbose_name='排序'),
        ),
    ]
