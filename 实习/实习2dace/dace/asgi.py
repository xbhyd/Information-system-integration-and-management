import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dace.settings')
application = get_asgi_application()  # 创建并返回一个ASGI应用实例，赋值给变量 application，用于处理ASGI请求
