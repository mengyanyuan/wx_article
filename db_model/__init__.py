# -*- encoding:utf-8 -*-
from django.apps import AppConfig
import os
from core_common.constants.constants import CommonConstants as Consts

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class PrimaryArticleConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = Consts.DJANGO_DB_MODEL_APP_NAME
