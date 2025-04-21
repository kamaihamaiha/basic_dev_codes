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
