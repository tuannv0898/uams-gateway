from django.db import models

# Create your models here.


class UhfRfModuleModel(models.Model):
    address = models.CharField(max_length=16)
    state = models.BooleanField(default=False)
