from django.db import models
import django.utils.timezone as timezone


class Type(models.Model):
    """文章类型表"""
    typeId = models.IntegerField(primary_key=True)
    typeName = models.CharField(max_length=32, blank=False, verbose_name='类型名称')
    status = models.CharField(max_length=4, blank=False, default='00', verbose_name='类型状态')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class User(models.Model):
    """用户表"""
    userId = models.CharField(max_length=15, primary_key=True, verbose_name='用户ID')
    openId = models.CharField(max_length=32, blank=False, verbose_name='微信小程序身份唯一标识')
    username = models.CharField(max_length=32, blank=False, verbose_name='用户名')
    head = models.CharField(max_length=32, verbose_name='用户头像')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    status = models.CharField(max_length=4, blank=False, default='00', verbose_name='账号状态（00-有效  01-注销）')
    lastLoginTime = models.DateTimeField(default=timezone.now, verbose_name='最后登录时间')


class Article(models.Model):
    """文章表"""
    articleId = models.CharField(max_length=36, primary_key=True, verbose_name='文章ID')
    articleType = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='文章类型')
    articleTags = models.CharField(max_length=20, blank=False, verbose_name='文章标签')
    title = models.CharField(max_length=255, blank=False, verbose_name='文章标题')
    content = models.TextField(blank=False, verbose_name='文章内容')
    date = models.DateTimeField(blank=False, default=timezone.now, verbose_name='发表时间')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    illustration = models.CharField(max_length=255, verbose_name='文章封面')
    status = models.CharField(max_length=4, default='01', verbose_name='文章状态（00-已发布  01-编辑中  02-审核中  99-已删除）')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modifyTime = models.DateTimeField(auto_now=True, verbose_name='修改时间')


class Banner(models.Model):
    """轮播图"""
    bannerId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, verbose_name='轮播图显示的标题')
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章ID')
    resurl = models.CharField(max_length=2048, verbose_name='资源路径')
    type = models.CharField(max_length=2, blank=False, verbose_name='显示类型（0-图片 1-视频）')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class Remark(models.Model):
    """评论表"""
    remarkId = models.CharField(max_length=36, primary_key=True, verbose_name='评论ID')
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章ID')
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户ID')
    content = models.TextField(max_length=255, blank=False, verbose_name='评论内容')
    status = models.CharField(max_length=4, blank=False, verbose_name='评论状态（00-有效  01-待审核  99-已删除）', default='01')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class Tag(models.Model):
    """标签表"""
    tagId = models.IntegerField(primary_key=True, verbose_name='标签ID')
    tagName = models.CharField(max_length=10, blank=False, verbose_name='标签名')
    status = models.CharField(max_length=4, blank=False, default='00', verbose_name='标签状态（00-有效  99-已删除）')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class LikeRel(models.Model):
    """点赞关系表"""
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章ID')
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户ID')
    status = models.CharField(max_length=4, verbose_name='状态（00-有效  01-失效）')

    class Meta:
        unique_together = ("userId", "articleId")
