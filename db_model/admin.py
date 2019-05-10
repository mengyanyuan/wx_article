from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from db_model.model_form.article_form import ArticleForm
from db_model.model_form.tag_form import TagForm
from db_model.model_form.type_form import TypeForm
from db_model.model_form.banner_form import BannerForm
from db_model.model_form.user_form import UserForm
from db_model.model_form.remark_form import RemarkForm
from db_model.model_form.likerel_form import LikeRelForm
from db_model.models import *
from core_common.utils.string_utils import String
from core_common.constants.constants import CommonConstants as Consts
from core_common.utils.config_parse import Configuration

config = Configuration.config()

# 设置网站信息
admin.site.site_header = config.get_value(Consts.DJANGO_SECTION, Consts.DJANGO_SITE_HEADER_NAME)
admin.site.site_title = config.get_value(Consts.DJANGO_SECTION, Consts.DJANGO_SITE_HEADER_TITLE)
verbose_name = Consts.DJANGO_DB_MODEL_APP_NAME


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 放在最上面，否则看不到自定义的表单
    form = ArticleForm
    list_display = ('title', 'author', 'status_name', 'date', 'createTime', 'modifyTime')
    fieldsets = (
        ('常规', {
            'fields': ('title', 'articleType', 'articleTags', 'content', 'date', 'status')
        }),
        ('高级选项', {
            'classes': ('collapse',),
            'fields': ('illustration',),
        }),
    )

    list_filter = ('articleType', 'status', 'articleType__typeName')
    search_fields = ('title', 'articleType__typeName', 'status')
    date_hierarchy = 'date'

    def save_model(self, request, obj, form, change):
        if change:
            if obj.status == '00':
                obj.date = timezone.now()
            obj.modifyTime = timezone.now()
            print(obj)
        else:
            article_id = String.random_id(length=10, start='210010') + String.get_timestamp(True)
            obj.articleId = article_id
            print(request.user.username)
            obj.author = request.user.userId
        obj.save()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    form = TagForm
    list_display = ('tagId', 'tagName', 'status_name', 'createTime')
    search_fields = ('tagName', 'tagId')

    def save_model(self, request, obj, form, change):
        if not change:
            print("要保存的对象：", obj)
            obj.save()


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    form = TypeForm
    list_display = ('typeId', 'typeName', 'status_name', 'createTime')
    search_fields = ('typeName', 'typeId')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    form = BannerForm
    list_display = ('title', 'articleId', 'resurl', 'type_name', 'createTime')
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        if not change:
            banner_id = String.get_timestamp(locallize=True) + String.random_id(6)
            obj.bannerId = banner_id
            print(len(obj.bannerId))
            obj.save()


@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ('userId', 'openId', 'username', 'head', 'status_name', 'last_login', 'date_joined')
    search_fields = ('userId', 'username', 'openId')

    fieldsets = (
        ('基本信息', {
            'fields': ('username', 'password', 'openId', 'is_active', 'is_staff')
        }),
        ('详细信息', {
            'classes': ('collapse',),
            'fields': ('first_name', 'last_name', 'email', 'head', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            user_id = obj.userId
            # 避免生成的Id在数据库内已存在
            while User.objects.filter(userId=user_id):
                user_id = String.random_id(length=10, start='10011')
            obj.userId = user_id
            obj.save()


@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    form = RemarkForm
    list_display = ('remarkId', 'articleId', 'userId', 'content', 'status_name')
    search_fields = ('remarkId', 'userId__username', 'userId__userId', 'articleId__title')


@admin.register(LikeRel)
class LikeRelAdmin(admin.ModelAdmin):
    form = LikeRelForm
    list_display = ('articleId', 'userId', 'type_name', 'status_name', 'createTime')
    search_fields = ('articleId__title', 'userId__userId', 'userId__username', 'type')
    list_filter = ('type', 'status')
    date_hierarchy = 'createTime'
