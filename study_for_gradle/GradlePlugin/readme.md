## 自定义插件

- [build.gradle 中编写](#buildgradle-中编写)
- [buildSrc 工程项目中编写](#buildsrc-工程项目中编写)
- [独立项目中编写](#独立项目中编写)


### build.gradle 中编写

[见 build.gradle 中的 CustomPlugin](./build.gradle)

```shell
# 终端中执行
gradle CustomPluginTask
```

输出结果:
```shell
Starting a Gradle Daemon (subsequent builds will be faster)

> Task :CustomPluginTask
自定义插件

BUILD SUCCESSFUL in 5s
1 actionable task: 1 executed
```

#### 自定义插件扩展
[见 build.gradle 中的 Humanlugin](./build.gradle)

```shell
# 在终端中执行
gradle HumanPluginTask
```

输出结果:
```shell
> Task :HumanPluginTask
自定义的HumanPlugin扩展

BUILD SUCCESSFUL in 716ms
1 actionable task: 1 executed
```

### buildSrc 工程项目中编写

[见 CustomPluginV2.groovy](buildSrc/src/main/groovy/CustomPluginV2.groovy)
要在 project 的 [build.gradle](./build.gradle) 中应用插件: `apply plugin: CustomPluginV2`
```shell
# 在终端中执行
gradle CustomPluginV2Task
```

### 独立项目中编写

- step1: [在一个独立项目中编写自定义插件](../GradlePluginShare/readme.md)
- step2: [在另一个项目中使用插件](../UsePluginDemo/readme.md)

