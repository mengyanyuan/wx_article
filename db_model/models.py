from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import format_html
from django.utils import timezone

from core_common.constants.constants import CommonConstants as Consts
from core_common.utils.config_parse import Configuration
from core_common.utils.string_utils import String

Config = Configuration.config()

STATUS_CHOICE = (
    ('00', '有效'),
    ('99', '已删除')
)
ARTICLE_STATUS = (
    ('00', '已发布'),
    ('01', '编辑中'),
    ('02', '审核中'),
    ('99', '已删除')
)
RESOURCE_TYPE = (
    ('0', '图片'),
    ('1', '视频')
)
REMARK_STATUS = (
    ('00', '有效'),
    ('01', '待审核'),
    ('99', '已删除')
)
LIKE_TYPE = (
    ('0', '点赞'),
    ('1', '收藏')
)


class Type(models.Model):
    """文章类型表"""
    typeId = models.AutoField(primary_key=True)
    typeName = models.CharField(max_length=32, verbose_name='类型名称')
    status = models.CharField(max_length=4, choices=STATUS_CHOICE, default='00', verbose_name='类型状态')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return str(self.typeId) + ' - ' + self.typeName

    def status_name(self):
        if self.status == '00':
            color_code = 'green'
            status_name = '有效'
        else:
            color_code = 'red'
            status_name = '已删除'
        return format_html('<span style="color: {};">{}（{}）</span>', color_code, status_name, self.status)

    status_name.short_description = u'状态'

    class Meta:
        verbose_name = "文章类型表"
        verbose_name_plural = verbose_name
        ordering = ['typeId']


class Tag(models.Model):
    """标签表"""
    tagId = models.AutoField(primary_key=True, verbose_name='标签ID')
    tagName = models.CharField(max_length=10, verbose_name='标签名')
    status = models.CharField(max_length=4, default='00', choices=STATUS_CHOICE, verbose_name='标签状态')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.tagName

    def status_name(self):
        if self.status == '00':
            color_code = 'green'
            status_name = '有效'
        else:
            color_code = 'red'
            status_name = '已删除'
        return format_html('<span style="color: {};">{}（{}）</span>', color_code, status_name, self.status)

    status_name.short_description = u'状态'

    class Meta:
        verbose_name = "文章标签表"
        verbose_name_plural = verbose_name
        ordering = ['tagId']


class User(AbstractUser):
    """用户表"""

    #  AbstractUser这个类，也就是Django框架默认使用的一个用于管理用户的User类，这个类生成一个auth_user表。
    # 所以，要扩展用户属性，可以继承AbstractUser，在子类UserModel中实现扩展。

    userId = models.CharField(max_length=15, primary_key=True, verbose_name='用户ID',
                              default=String.random_id(length=10, start='1001'))
    openId = models.CharField(max_length=32, verbose_name='微信小程序身份唯一标识')
    # username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=128, default='Passw0rd123', verbose_name='用户密码')
    head = models.ImageField(upload_to=Config.get_value(Consts.DJANGO_SECTION, Consts.DJANGO_PATH_HEAD) + '%Y/%m/%d',
                             null=True,
                             blank=True, verbose_name='用户头像')
    # status = models.CharField(max_length=4, default='00', choices=STATUS_CHOICE, verbose_name='账号状态')
    AbstractUser.date_joined = models.DateTimeField(auto_now_add=True, default=timezone.now)

    def __str__(self):
        return self.username + '（' + self.userId + '）'

    def status_name(self):
        if AbstractUser.is_active == 1:
            color_code = 'green'
            status_name = '有效'
        else:
            color_code = 'red'
            status_name = '注销'
        return format_html('<span style="color: {};">{}（{}）</span>', color_code, status_name, AbstractUser.is_active)

    status_name.short_description = u'账号状态'

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        ordering = ['-userId']


class Article(models.Model):
    """文章表"""
    articleId = models.CharField(max_length=36, primary_key=True, verbose_name='文章ID')
    articleType = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='文章类型')
    # articleTags = models.CharField(max_length=20,  verbose_name='文章标签')
    articleTags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=255, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    date = models.DateTimeField(null=True, blank=True, verbose_name='发表时间')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    illustration = models.ImageField(
        upload_to=Config.get_value(Consts.DJANGO_SECTION, Consts.DJANGO_PATH_ILLUSTRATIONS) + '%Y/%m/%d', null=True,
        blank=True,
        verbose_name='文章封面')
    status = models.CharField(max_length=4, default='01', blank=False, choices=ARTICLE_STATUS, verbose_name='文章状态')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modifyTime = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')

    def __str__(self):
        return self.title + '（' + self.articleId + '）'

    def status_name(self):
        if self.status == '00':
            color_code = 'green'
            status_name = '已发布'
        elif self.status == '01':
            color_code = 'blue'
            status_name = '编辑中'
        elif self.status == '02':
            color_code = 'yellow'
            status_name = '审核中'
        else:
            color_code = 'red'
            status_name = '已删除'
        return format_html('<span style="color: {};">{}（{}）</span>', color_code, status_name, self.status)

    status_name.short_description = u'文章状态'

    class Meta:
        verbose_name = "文章表"
        verbose_name_plural = verbose_name
        ordering = ['-date']


class Banner(models.Model):
    """轮播图"""
    bannerId = models.CharField(primary_key=True, max_length=26)
    title = models.CharField(max_length=255, verbose_name='轮播图显示的标题')
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='文章ID')
    resurl = models.FileField(upload_to=Config.get_value(Consts.DJANGO_SECTION, Consts.DJANGO_PATH_FILE) + '%Y/%m/%d',
                              blank=True,
                              null=True, verbose_name='资源路径')
    type = models.CharField(max_length=2, choices=RESOURCE_TYPE, default='0', verbose_name='资源类型')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def type_name(self):
        if self.type == '0':
            color_code = 'green'
            type_name = '图片'
        else:
            color_code = 'blue'
            type_name = '视频'
        return format_html('<span style="color: {};">{} - {}</span>', color_code, self.type, type_name)

    type_name.short_description = u'资源类型'

    class Meta:
        verbose_name = "轮播图表"
        verbose_name_plural = verbose_name
        ordering = ['-createTime']


class Remark(models.Model):
    """评论表"""
    remarkId = models.CharField(max_length=36, primary_key=True, verbose_name='评论ID')
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    content = models.TextField(max_length=255, verbose_name='评论内容')
    status = models.CharField(max_length=4, verbose_name='评论状态', choices=REMARK_STATUS, default='01')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def status_name(self):
        if self.status == '00':
            color_code = 'green'
            status_name = '有效'
        elif self.status == '01':
            color_code = 'blue'
            status_name = '待审核'
        else:
            color_code = 'red'
            status_name = '已删除'
        return format_html('<span style="color: {};">{}（{}）</span>', color_code, status_name, self.status)

    status_name.short_description = u'评论状态'

    class Meta:
        verbose_name = "评论表"
        verbose_name_plural = verbose_name
        ordering = ['-createTime']


class LikeRel(models.Model):
    """点赞与收藏关系表"""
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    type = models.CharField(max_length=4, default='0', verbose_name='类型', choices=LIKE_TYPE)
    status = models.CharField(max_length=4, verbose_name='状态', choices=STATUS_CHOICE, default='00')
    createTime = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    def type_name(self):
        if self.type == '0':
            color_code = 'green'
            type_name = '点赞'
        else:
            color_code = 'blue'
            type_name = '收藏'
        return format_html('<span style="color: {};">{}（{}）</span>', color_code, type_name, self.type)

    def status_name(self):
        if self.status == '00':
            color_code = 'green'
            status_name = '有效'
        else:
            color_code = 'red'
            status_name = '取消'
        return format_html('<span style="color: {};">{}（{}）</span>', color_code, status_name, self.status)

    type_name.short_description = u'类型'
    status_name.short_description = u'状态'

    class Meta:
        unique_together = ("userId", "articleId", "type")
        verbose_name = "点赞与收藏关系表"
        verbose_name_plural = verbose_name
