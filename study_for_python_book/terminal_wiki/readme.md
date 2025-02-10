## 终端中运行 python


### apple m 处理器设备

运行python代码，要指定用 arm64
``arch -arm64 python3 rw_demo.py ``


### 安装 matplotlib

``python3 -m pip install matplotlib --trusted-host mirrors.aliyun.com``

### Pygal 画廊
要了解使用Pygal可创建什么样的图表，请查看图表类型画廊：访问http://www.pygal.org/，单击Documentation，再单击Chart types。每个示例都包含源代码，让你知道这些图表是如何生成的

### mac ox 安装 Pygal

- 创建虚拟环境
	- python3 -m venv myenv // 如果有了，则不用创建
	- source ~/myenv/bin/activate
	- python3 -m pip install pygal==1.7 --trusted-host mirrors.aliyun.com
- 安装 arm64架构的
   - ``arch -arm64 python3 -m pip install pygal==1.7``
- 查看 pygal 安装情况
   - ``pip show pygal``

#### pygal + python 3.10+ 报错处理

- pygal 代码中使用了 from collections import Iterable，但 Iterable 在 Python 3.10 及以上版本中已经被移到了 collections.abc 模块，导致 ImportError

解决:
1. 修改 pygal 代码，使其兼容 Python 3.10+：
    - pygal/_compat.py 文件
    - ``from collections import Iterable`` 修改为: ``from collections.abc import Iterable``

2. 且升级 pygal: ``python3 -m pip install --upgrade pygal --trusted-host mirrors.aliyun.com``




