## Gradle 插件

- [什么是Gradle插件](#什么是gradle插件)
- [应用Gradle插件](#应用gradle插件)
- [插件DSL](#插件dsl)
- [自定义对象插件](#自定义对象插件)

### 什么是Gradle插件

Gradle 插件是一种扩展 Gradle 构建工具功能的机制。


### 应用Gradle插件

- step1: 解析插件；
- step2: 应用到项目中
  - ``Project.apply()``

#### 一般有2种类型的插件

- [脚本插件, 见 other.gradle](./g_plugin/other.gradle)
- 对象插件
  - 也叫二进制插件，实现了 `Plugin` 接口

##### 对象插件

- 实现了 ``org.gradle.api.Plugin<Project>`` 接口的插件
- 可以分为: 内部插件和第三方插件

###### 内部插件

```groovy
// 使用JavaPlugin
apply plugin: org.gradle.api.plugins.JavaPlugin
// 简写
apply plugin: JavaPlugin

// 通过 plugin id 方式
apply plugin: 'java'

// 想在项目中有cpp代码编译功能，可以引入 cpp插件
apply plugin: 'cpp'
```


###### 第三方插件

通常是jar包形式，要用 ``buildscript`` 定义插件所在的仓库和依赖

引入 com.jfrog.bintray 插件
```groovy
buildscript {
  repositories {
    maven {
      url "https://plugins.gradle.org/m2/"
    }
  }

  dependencies {
    classpath "com.jfrog.bintray.gradle:gradle-bintray-plugin:1.8.4"
  }
}

apply plugin: "com.jfrog.bintray"
```

引入 android gradle 插件:

    


### 插件DSL

DSL: domain specific language(领域专用语言)

Gradle 的特性有四种状态: Internal, Incubating, Public, Deprecated

插件DSL 属于 Incubating(孵化状态)；不断变化

```groovy
plugins {
  id 'java'
  id "com.jfrog.bintary" version "1.8.4"
}
```


### 自定义对象插件

