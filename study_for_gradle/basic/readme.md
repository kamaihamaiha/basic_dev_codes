## Gradle 基础知识


- Gradle 任务
- Gradle 日志级别
- Gradle 命令行


---

### Gradle 任务

#### 创建 Gradle 任务

多 种方式, 见[ build.gradle](./build.gradle)

#### 任务分组和描述

见[ build.gradle](./build.gradle)


### 日志级别

- Error
- Quiet: 重要的信息消息
- Warning
- Lifecycle: 进度信息消息
- Info
- Debug

#### Gradle 开关选项

- 无日志选项: Lifecycle 及更高级别
- `-q`或`-quiet`: Quiet 及更高级别
- `-i`或`-info`: Info 及更高级别
- `-d`或`-debug`: Debug 及更高级别

### Gradle 命令行

- 获取所有的任务信息: ``gradle -q tasks``
  - 默认显示的分组的任务
- 获取任务帮助信息: ``gradle -q help --task hello``
- 多任务调用: ``gradle hello good``
  - 任务之间空格隔开
- 任务名称缩写

#### 任务名称缩写

 





