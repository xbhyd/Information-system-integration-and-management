from django.urls import include, path
from rest_framework import routers
from . import views

# 配置路由
router = routers.DefaultRouter()  # 创建一个默认路由器
router.register(r'Student', views.StudentViewSet)  # 将StudentViewSet视图集注册到路由器，路径为/Student/

urlpatterns = [
    path('', include(router.urls)),  # 将路由器的路由添加到URL模式中
    path('api/', include('rest_framework.urls', namespace='rest_framework'))  # 添加RESTful API认证和授权
]
