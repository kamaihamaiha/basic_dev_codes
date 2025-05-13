"""定义learning_logs的URL模式"""

# 导入函数 url
from django.urls import path

# 导入模块 views
from . import views

urlpatterns = [
    # 主页
    path(r'', views.index, name='index'),

    # 显示所有的主题
    path(r'topics/', views.topics, name='topics')
]


