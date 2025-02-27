from django.contrib import admin
from django.urls import path, include

# 全局路由
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dace01.urls')),
]
