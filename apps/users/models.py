from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_CHOICES = (
    ('male', '男'),
    ('female', '女')
)


class BaseModel(models.Model):
    # verbose_name 修改后台系统字段为定义内容
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        # 将该基类定义为抽象类，目的不生成表单，只作为一个可以继承的基类
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=GENDER_CHOICES)
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    image = models.ImageField(verbose_name='用户头像', upload_to='head_image/%Y/%m', default='default.jpg')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

        # def unread_nums(self):
        #    """
        #    未读消息数量
        #    :return:
        #    """
        #    return self.usermessage_set.filter(has_read=False).count()
        def __str__(self):
            if self.nick_name:
                return self.nick_name
            else:
                return self.username
