from django.db import models
from users.models import UserInfo


# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    marker = models.CharField(max_length=100, default="undefined")
    is_processed = models.BooleanField(default=False)
    processing = models.BooleanField(default=False)

    def image_upload_path(self, filename):
        user_folder = f'user_{self.user.id}'
        return f'static/images/{user_folder}/{filename}'

    image_path = models.ImageField(upload_to=image_upload_path)

    def __str__(self):
        return f"User: {self.user.username}"


class MarkerTxtPath(models.Model):
    marker = models.CharField(max_length=100, default="undefined")
    txt_path = models.FileField(upload_to='static/txt/', null=True, blank=True)

    def __str__(self):
        return f"Txt: {self.txt_path}, Marker: {self.marker}"
