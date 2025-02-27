from django.db import models


# 定义了一个名为Student的模型
class Student(models.Model):
    name = models.CharField(max_length=8, null=False, verbose_name='姓名')
    num = models.CharField(max_length=13, null=False, verbose_name='学号')
    email = models.EmailField(null=False, verbose_name='邮箱')
    mobile = models.CharField(max_length=11, null=False, verbose_name='手机号码')
    hobbit = models.CharField(max_length=32, null=False,verbose_name='爱好')
