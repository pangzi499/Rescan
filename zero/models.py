# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class zeroHistory(models.Model):
    xTarget = models.CharField('Target',max_length=30)
    xType = models.CharField('Type',max_length=30)
    xInfo = models.CharField('Info',max_length=10)

    class Meta:
        db_table = 'zeroHistory'