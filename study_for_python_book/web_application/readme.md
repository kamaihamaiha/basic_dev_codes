## Web 应用

### chapter 18 Django

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
