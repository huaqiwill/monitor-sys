from django.shortcuts import render
from django.core.paginator import Paginator
from .utils.mail import EMail
from common.API import res_josn_data
from common.API.auth import authorize, login_required
from login.models import Log
import json
from .models import Monitor, Notify
from django.http import JsonResponse


def ratelimit_handler(request):
    """访问限制处理工具"""
    return JsonResponse({"error": "Too many requests. Please try again later."})


# Create your views here.
@login_required
def monitor(request):
    """事件监控预警"""
    return render(request, "monitor/monitor.html")


@login_required
def monitor_query(request):
    """监控预警查询"""
    # if request.method != "POST":
    #     return res_josn_data.fail_api("不支持的请求格式")

    # 获取必填参数
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    user_obj = Monitor.objects.filter().order_by("id")
    page_data = Paginator(user_obj, limit).page(page)

    # 序号
    count = (int(page) - 1) * int(limit)

    return res_josn_data.table_api(count=len(user_obj), data=page_data)


@login_required
def monitor_delete(request):
    return res_josn_data.success_api("success")


@login_required
def notify(request):
    """通知管理"""
    # EMail().send_email()
    return render(request, "monitor/notify.html")


@login_required
def notify_query(request):
    return res_josn_data.success_api("success")


@login_required
def notify_delete(request):
    return res_josn_data.success_api("success")


@login_required
def handle(request):
    return render(request, "monitor/handle.html")


@login_required
def handle_query(request):
    return res_josn_data.success_api("success")


@login_required
def handle_delete(request):
    return res_josn_data.success_api("success")


@login_required
def recover(request):
    return render(request, "monitor/recover.html")


@login_required
def recover_query(request):
    return res_josn_data.success_api("success")


@login_required
def recover_delete(request):
    return res_josn_data.success_api("success")


from .utils import sqlbak


def mysql_backup(request):
    sqlbak.backup()


def mysql_restore(request):
    sqlbak.restore()


from .models import Attack
import psutil


def dashboard(request):
    return render(request, "monitor/dashboard.html")


def get_attack_data(request):
    attacks = Attack.objects.all().values("attack_type", "timestamp", "description")
    return JsonResponse(list(attacks), safe=False)


def get_system_data(request):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")
    system_data = {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_info.percent,
        "disk_usage": disk_usage.percent,
    }
    return JsonResponse(system_data)


def restore_page(request):
    return render(request, "monitor/recover.html")


from .models import RestoreRecord


def get_restore_records(request):
    records = RestoreRecord.objects.all().values(
        "timestamp", "filename", "status", "details"
    )
    return JsonResponse(list(records), safe=False)
