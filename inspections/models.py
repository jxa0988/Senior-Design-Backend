from django.conf import settings
from django.db import models

class InspectionCase(models.Model):
    # “Client house” — title can be address or custom label
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ImageAsset(models.Model):
    case = models.ForeignKey(InspectionCase, on_delete=models.CASCADE, related_name="images")
    # store file path; DRF will save to MEDIA_ROOT
    file = models.ImageField(upload_to="cases/%Y/%m/%d/")  # simple local path
    status = models.CharField(max_length=32, default="uploaded")
    uploaded_at = models.DateTimeField(auto_now_add=True)
