# Generated by Django 4.1.7 on 2024-05-26 01:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=10, verbose_name='请求方法')),
                ('uid', models.CharField(max_length=10, verbose_name='用户ID')),
                ('url', models.CharField(max_length=50, null=True, verbose_name='请求URL')),
                ('desc', models.TextField(null=True, verbose_name='备注')),
                ('ip', models.CharField(max_length=30, null=True, verbose_name='请求方法')),
                ('success', models.IntegerField(null=True, verbose_name='是否成功')),
                ('user_agent', models.CharField(max_length=255, null=True, verbose_name='请求方法')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'sys_log',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='菜单名称')),
                ('desc', models.CharField(max_length=50, null=True, verbose_name='菜单描述')),
                ('type', models.IntegerField(null=True, verbose_name='菜单类型')),
                ('url', models.CharField(max_length=50, null=True, verbose_name='菜单url')),
                ('parent_id', models.IntegerField(null=True, verbose_name='父级id')),
                ('icon', models.CharField(max_length=50, null=True, verbose_name='图标')),
                ('sort', models.IntegerField(null=True, verbose_name='排序')),
            ],
            options={
                'db_table': 'web_logo',
            },
        ),
    ]
