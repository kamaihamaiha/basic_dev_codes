## Gradle Wrapper

为什么需要 Gradle Wrapper

Gradle Wrapper 是一个脚本，可以在计算机没有安装 Gradle 的情况下运行Gradle构建，并且能够指定Gradle的版本，
开发人员可以快速启动并运行Gradle项目，不必手动安装，这样就标准化了项目。

### 构建 Gradle Wrapper
前提当前目录下有 build.gradle
```shell
# 自带的内置任务 wrapper
gradle wrapper
```
生成如下文件:
```shell
├── gradle
│         └── wrapper
│             ├── gradle-wrapper.jar
│             └── gradle-wrapper.properties
├── gradlew
└── gradlew.bat

```

### gradle 命令行选项

- ``--gradle-version``: 用于下载和执行指定的Gradle版本
- ``--distribution-type``: 指定下载Gradle发型版的类型，可用选项有bin和all，默认是bin（只包含运行时，不包含源码和文档）；
- ``--gradle-distribution-url``: 指定下载Gradle发行版的完整URL地址
- ``--gradle-distribution-sha256-sum``: 使用的SHA 256散列和验证下载的Gradle发行版

### 通过 gradle 命令更新 Gradle 方式

- 方式1
  - ``./gradlew fooTask`` 
  - 前提是在 gradle-wrapper.properties 指定distributionUrl为新的版本
- 方式2
  - ``./gradlew wrapper --gradle-version 新版本``
  - 接着执行 ``./gradlew -v`` 就开始下载了