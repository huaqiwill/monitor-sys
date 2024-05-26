# Generated by Django 4.1.7 on 2024-05-26 01:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='权限名称')),
                ('type', models.IntegerField(verbose_name='权限类型')),
                ('code', models.CharField(max_length=30, null=True, verbose_name='权限标识')),
                ('url', models.CharField(max_length=30, null=True, verbose_name='权限路径')),
                ('open_type', models.CharField(max_length=20, null=True, verbose_name='权限类型-中文')),
                ('parent_id', models.IntegerField(null=True, verbose_name='父类编号')),
                ('icon', models.CharField(max_length=50, null=True, verbose_name='图标')),
                ('sort', models.IntegerField(null=True, verbose_name='排序')),
                ('enable', models.IntegerField(default=1, verbose_name='是否开启')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'sys_power',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_value', models.IntegerField(verbose_name='角色值')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='角色名称')),
                ('code', models.CharField(max_length=50, verbose_name='角色标识')),
                ('enable', models.IntegerField(verbose_name='是否启用')),
                ('remark', models.CharField(max_length=255, null=True, verbose_name='备注')),
                ('details', models.CharField(max_length=255, null=True, verbose_name='详情')),
                ('sort', models.IntegerField(null=True, verbose_name='排序')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'sys_role',
            },
        ),
        migrations.CreateModel(
            name='RolePower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField(verbose_name='角色id')),
                ('power_id', models.IntegerField(verbose_name='权限id')),
                ('power_type', models.IntegerField(verbose_name='类型')),
            ],
            options={
                'db_table': 'role_power',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=30, verbose_name='用户账号')),
                ('id_password', models.CharField(max_length=255, verbose_name='用户密码')),
                ('user_name', models.CharField(max_length=30, verbose_name='用户名称')),
                ('department', models.CharField(blank=True, max_length=50, null=True, verbose_name='部门')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='职位')),
                ('role_id', models.IntegerField(null=True, verbose_name='角色id')),
                ('role_des', models.CharField(max_length=30, null=True, verbose_name='角色描述')),
                ('user_status', models.IntegerField(default=1, verbose_name='用户状态')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'sys_user',
            },
        ),
    ]
