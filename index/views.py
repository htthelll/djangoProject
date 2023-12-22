from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from djangoProject import settings
from .models import *
from users.models import UserInfo
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.core.files.storage import default_storage
import os
from django.http import JsonResponse
from .task import process
import shutil
import zipfile


# Create your views here.


@login_required
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        uploaded_images = request.FILES.getlist('image')
        _id = request.session['id']
        current_user = UserInfo.objects.get(id=_id)
        marker = request.POST.get('text')
        if Image.objects.filter(marker=os.path.join(str(_id), marker)).count() > 0:
            HttpResponse("名称重复，请重新输入")
        for image in uploaded_images:
            Image.objects.create(user=current_user, image_path=image, marker=(str(_id) + '-' + marker))
        return HttpResponseRedirect('/')


def image_gallery(request):
    user_id = request.session.get('id')

    if user_id is not None:
        images_by_marker = {}
        images = Image.objects.filter(user_id=user_id).order_by('marker')
        for image in images:
            if image.marker.split('-')[1] not in images_by_marker:
                # images_by_marker[image.marker.split('-')[1]] = []
                group_images = Image.objects.filter(marker=image.marker)
                images_by_marker[image.marker.split('-')[1]] = {
                    'image': image,
                    'is_processed': image.is_processed,
                    'processing': image.processing,
                    'count': group_images.count(),
                    'data_name': image.marker
                }

        context = {'images_by_marker': images_by_marker}
        return render(request, 'zhanshi.html', context)
    else:
        return HttpResponse("请先登录")


def detect_marker_images(request, marker):
    images = Image.objects.filter(marker=marker).order_by('marker')
    images.update(processing=True)
    process.delay(marker)
    return JsonResponse({'status': 'success'})


def download_marker_images(request, marker):
    if marker is not None:
        zip_dir = os.path.join(settings.BASE_DIR, 'temp_zip')
        zip_filename = f'{marker}_data'
        zip_path = os.path.join(zip_dir, zip_filename)
        # 读取压缩文件
        response = FileResponse(open(zip_path + '.zip', 'rb'), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{zip_filename}.zip"'

        return response
    else:
        # 处理未提供marker参数的情况
        return HttpResponse("Marker parameter is missing.", status=400)


def delete_marker_images(request, marker):
    records_to_delete = Image.objects.filter(marker=marker).order_by('marker')
    for record in records_to_delete:
        image_path = record.image_path.path
        if default_storage.exists(image_path):
            default_storage.delete(image_path)
    records_to_delete.delete()

    txt_to_delete = MarkerTxtPath.objects.filter(marker=marker).order_by('marker')
    for record in txt_to_delete:
        txt_path = record.txt_path.path
        if default_storage.exists(txt_path):
            default_storage.delete(txt_path)
    txt_to_delete.delete()

    zip_filename = f'{marker}_data'
    zip_dir = os.path.join(settings.BASE_DIR, 'temp_zip')
    zip_path = os.path.join(zip_dir, zip_filename)
    if default_storage.exists(zip_path + '.zip'):
        default_storage.delete(zip_path + '.zip')
    return JsonResponse({'status': 'success'})
