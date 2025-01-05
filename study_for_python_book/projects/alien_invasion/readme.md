## 外星人项目


- 需要安装 pygame 库


### mac ox 安装 pygame

- 方式一: pip3 install pygame 出错: Externally-Managed-Environment 
- 方式二: 创建虚拟环境
	- python3 -m venv myenv
	- source ~/myenv/bin/activate
	- python3 -m pip install pygame --trusted-host mirrors.aliyun.com

#### 查看pygame 安装情况

- 激活虚拟环境: ``source ~/myenv/bin/activate``
- 显示信息：pip show pygame
- 或者启动 Python终端会话, 导入 pygame
	- python3
	- import pygame	
- 退出虚拟环境: ``deactivate``	

