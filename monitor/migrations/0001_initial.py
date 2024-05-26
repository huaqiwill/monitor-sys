# Generated by Django 4.1.7 on 2024-05-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(verbose_name='请求时间')),
                ('request_method', models.CharField(max_length=10)),
                ('request_path', models.CharField(max_length=255)),
                ('response_status', models.IntegerField()),
                ('response_time', models.FloatField()),
                ('disposal_time', models.DateTimeField()),
                ('source_ip', models.GenericIPAddressField()),
                ('attack_type', models.CharField(max_length=10)),
                ('details', models.TextField()),
                ('auto_handled', models.BooleanField()),
                ('handled_status', models.CharField(max_length=20)),
                ('handled_action', models.TextField()),
                ('handled_details', models.TextField()),
                ('filename', models.CharField(max_length=255, verbose_name='备份文件名')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='备份时间')),
                ('status', models.CharField(choices=[('SUCCESS', 'Success'), ('FAILED', 'Failed')], max_length=10, verbose_name='处置状态')),
                ('is_restore', models.IntegerField(verbose_name='是否恢复')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200, verbose_name='用户ID')),
                ('request_url', models.CharField(max_length=200, verbose_name='请求URL')),
                ('request_method', models.CharField(max_length=200, verbose_name='请求方法')),
                ('request_data', models.CharField(max_length=200, verbose_name='携带数据')),
                ('request_ip', models.CharField(max_length=200, verbose_name='请求来源IP')),
                ('attack_type', models.CharField(choices=[('XSS', 'XSS Attack'), ('CSRF', 'CSRF Attack'), ('SQLI', 'SQL Injection')], max_length=10, verbose_name='攻击类型')),
                ('attack_time', models.DateTimeField(auto_now_add=True, verbose_name='攻击事件')),
                ('description', models.TextField(verbose_name='事件描述')),
            ],
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_type', models.CharField(max_length=200, verbose_name='通报类型')),
                ('notify_mail', models.CharField(max_length=200, verbose_name='通报邮箱')),
                ('notify_subject', models.CharField(max_length=200, verbose_name='通报主题')),
                ('notify_content', models.CharField(max_length=200, verbose_name='通报内容')),
                ('notify_time', models.DateTimeField(max_length=200, verbose_name='通报时间')),
                ('notify_status', models.CharField(max_length=200, verbose_name='通报状态')),
            ],
        ),
        migrations.CreateModel(
            name='SubEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_email', models.CharField(max_length=200, verbose_name='订阅者邮件')),
                ('sub_status', models.IntegerField(verbose_name='订阅状态')),
                ('sub_date', models.DateField(verbose_name='订阅日期')),
                ('sub_name', models.CharField(max_length=200, verbose_name='订阅人')),
                ('user_id', models.CharField(max_length=200, verbose_name='当前用户ID')),
            ],
        ),
    ]
