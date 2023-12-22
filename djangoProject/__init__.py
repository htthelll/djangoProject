from __future__ import absolute_import, unicode_literals

# 这会确保在启动 Django 时，Celery应用会被自动加载
from .celery import app as celery_app

__all__ = ('celery_app',)
