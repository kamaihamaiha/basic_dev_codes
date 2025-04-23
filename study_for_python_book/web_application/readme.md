## Web 应用

### chapter 18 Django

#### 1. 建立项目(learning_log)

- 建立虚拟环境: `python3 -m venv ll_env`
- 激活虚拟环境: `source ll_env/bin/activate`
- 停止虚拟环境: `deactivate` 或者关闭运行虚拟环境的终端
  - 查看虚拟环境是否激活
    - `echo $VIRTUAL_ENV`           # 显示虚拟环境路径（空则表示未激活）
    - `which python`                # 检查当前使用的 Python 路径
    - `pip -V`                      # 查看 pip 关联的 Python 路径
- 安装 Django: `pip install Django`
- 在 Django 中创建项目
  - 创建名为 learning_log 的项目: `django-admin startproject learning_log .`
  - 创建一个数据库: `python manage.py migrate`
  - 核实Django是否创建了项目,执行命令: `python manage.py runserver`
    - 输出如下:
      - ```
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced). # Django通过检查确认正确创建了项目
        April 21, 2025 - 00:24:47
        Django version 5.2, using settings 'learning_log.settings' # 指出使用的Django版本以及当前使用的设置文件名称
        Starting development server at http://127.0.0.1:8000/ # 指出项目的URL
        Quit the server with CONTROL-C.
        ```

#### 2. 创建应用程序

Django项目由一系列应用程序组成，他们协同工作，让项目成为一个整体。

##### 创建应用程序所需的基础设施 

- 新开一个终端
- 激活虚拟环境
- 执行命令: `python manage.py startapp learning_logs`
- 会生成文件夹 learning_logs
  - 包含重要的文件: models.py, admin.py, views.py
- 定义模型: 在 models.py 中，定义 Topic 类
- 激活模型: 在 settings.py 的 INSTALL_APPS 中添加: 'learning_logs'
- 让 Django 修改数据库，使其能够存储与模型Topic相关的信息
  - `python manage.py makemigrations learning_logs`
  - 上面的命令让Django确定该如何修改数据库，生成一个迁移文件: `learning_logs/migrations/0001_initial.py`，这个文件将
    在数据库中为模型Topic创建一个表
  - 应用这种迁移，让Django替我们修改数据库: `python manage.py migrate` 
    - 注意这个输出，说明迁移正常: `Applying learning_logs.0001_initial... OK`

**注意：**
每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：修改models.py；对learning_logs调用makemigrations；让Django迁移项目

##### 管理网站

- 创建超级用户
  - `python manage.py createsuperuser`
  - username: kk
  - email: gmail.com
  - pwd: zkx_2025

- 向管理网站注册模型
  - learning_logs 项目里 admin.py 操作
  - 然后运行服务，打开: 127.0.0.1:8000/admin/
    - 就能输入超级管理员账号登录


#### 模型 Entry

- 定义
- 迁移
- 注册


#### Django shell

通过交互式终端以编程的方式查看数据。

example:
```shell
python manage.py shell                 
8 objects imported automatically (use -v 2 for details).

Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
>>> 
```
- `python manage.py shell`: 启动 Django shell
- `from learning_logs.models import Topic`: 导入模块learning_logs.models中的Topic模型
- `Topic.objects.all()`: 获取模型Topic的所有实例; 返回的是列表，称为查询集(queryset)
- `Ctrl + D`: 中止shell

#### Django API
 [查询数据文档](https://docs.djangoproject.com/en/5.2/topics/db/queries/)