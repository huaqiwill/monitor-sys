# PyMonitorSystem 基于Django的网络安全事件应急响应与处置系统

SystemMonitor

系统监控工具，使用Python Django开发完成

系统服务监控系统

安装依赖
```
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

运行项目

```
python manage.py runserver --insecure localhost:8080
```

#### 介绍

一个利用后端Django+前端layui,数据库用Mysql的网络安全事件应急响应与处置系统系统。一个很不错的Django学习项目。

#### 功能

* 事件监控预警：监控常见的网络攻击（SQL注入、XSS攻击、CSRF注入等）
* 安全事件通报：通报记录，邮件提醒（当监控到有网络攻击时，通报给订阅的用户）
* 应急响应处置：处置记录，数据库实时备份记录（当监控到网络攻击时，进行相应的处理操作）
* 数据业务恢复：数据库恢复记录（根据数据库备份记录，进行数据库还原操作）

部署在docker中

* 时间
* CPU使用率
* 内存使用率
* 磁盘使用率
* 网络流入
* 网络流出

* 请求时间
* 请求方法
* 请求路径
* 响应状态
* 响应时间
* 处置时间
* 源IP
* 攻击类型
* 详情
* 是否自动处理
* 处理状态
* 处理动作
* 处理详情

* 时间
* 攻击记录ID
* 应急响应动作
* 已解决
* 解决详情
* 响应人

#### 脚本

1. 执行`01_install.bat`安装项目依赖
2. 执行`02_run.bat`启动项目
3. 访问 http://127.0.0.1:8000/
4. 管理员账号：admin  密码：admin


扩展功能

 - CPU 负荷
 - 内存使用
 - 磁盘使用
 - 网络状况
 - 端口监视
 - 进程监视
 - 流量统计

#### futures


#### 软件架构


#### 安装教程



#### 使用说明



