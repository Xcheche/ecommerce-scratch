from django.db import models

from django.utils import timezone


class BaseModel(models.Model):
    # overiding the default id field to make it a UUID field which is secured
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        abstract = True