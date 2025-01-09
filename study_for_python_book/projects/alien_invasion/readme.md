## 外星人项目


- 需要安装 pygame 库


### mac ox 安装 pygame

- 方式一: pip3 install pygame 出错: Externally-Managed-Environment 
- 方式二: 创建虚拟环境
	- python3 -m venv myenv
	- source ~/myenv/bin/activate
	- python3 -m pip install pygame --trusted-host mirrors.aliyun.com
- 在 Apple m系列电脑安装说明	


#### 查看pygame 安装情况

- 激活虚拟环境: ``source ~/myenv/bin/activate``
- 显示信息：pip show pygame
- 或者启动 Python终端会话, 导入 pygame
	- python3
	- import pygame	
- 退出虚拟环境: ``deactivate``	

### 配置 sublime Text 构建系统，以便使用虚拟环境的 python

- Tools > Build System > New Build System
- 在新打开的文件中输入以下内容：
	```
	{
		"cmd": ["/Users/kk/myenv/bin/python3", "-u", "$file"],
	    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
	    "selector": "source.python",
	    "env": {
	        "PYTHONPATH": "/Users/kk/myenv/lib/python3.10/site-packages"
	    }
	}
	```
	- cmd：指定虚拟环境的 Python 路径
	- PYTHONPATH：确保 Sublime 知道虚拟环境的包路径
- 保存文件为 venv_python.sublime-build
	- 默认存储路径： ``~/Library/Application Support/Sublime Text 3/Packages/User``

#### Apple M处理器设备上 安装 pygame

- 先安装 pygame 依赖库: ``arch -arm64 brew install hg sdl sdl_image sdl_ttf``
- 安装 arm64 架构的 pygame: ``arch -arm64 python3 -m pip install pygame --force-reinstall --no-cache-dir``
	- 前面已经安装了 x86 的pygame, 所以加了 --force-reinstall 参数

