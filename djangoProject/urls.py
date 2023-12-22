"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from index import views as index_view

urlpatterns = [
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', index_view.index, name='index'),
    path('zhanshi/', index_view.image_gallery, name='history'),
    path('up_load/', index_view.index, name='upload'),
    path('detect_marker_images/<str:marker>/', index_view.detect_marker_images, name='detect_marker_images'),
    path('download_marker_images/<str:marker>/', index_view.download_marker_images, name='download_marker_images'),
    path('delete_marker_images/<str:marker>/', index_view.delete_marker_images, name='delete_marker_images')
]
