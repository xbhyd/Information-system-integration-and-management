from rest_framework import serializers
from .models import Student


# 定义了一个名为StudentSerializer的类，继承自serializers.HyperlinkedModelSerializer。该类用于序列化和反序列化Student模型的数据
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'num', 'email', 'mobile', 'hobbit')
