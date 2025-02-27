from rest_framework import viewsets
from .serializer import StudentSerializer
from .models import Student


# 建立视图
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('num')  # 排序
    serializer_class = StudentSerializer  # 序列化器
