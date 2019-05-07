from django.contrib import admin
from db_model.models import *

# Register your models here.
admin.site.register([Article, Banner, Remark, Tag, Type, User, LikeRel])
