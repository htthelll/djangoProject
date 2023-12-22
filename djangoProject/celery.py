from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 设置 Django 的配置模块并启动 Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

# 创建 Celery 应用
app = Celery('djangoProject')

# 使用 Django 设置模块
app.config_from_object('django.conf:settings', namespace='CELERY')

# 从所有注册的 Django app 中加载任务模块
app.autodiscover_tasks()
