## Android Gradle Plugin


- [AS的模块类型和项目视图](#as的模块类型和项目视图)
- 项目build.gradle
- [模块build.gradle](#模块buildgradle)
- [Android签名文件配置](#android签名文件配置)
- Gradle的库依赖
- Gradle的库依赖管理

---
### 介绍

- Gradle有很多插件，为了支持Android项目的构建，Google为Gradle编写了Android插件。
- Android studio 使用Gradle wrapper来集成Gradle的Android插件；Gradle的Android插件可以独立于Android Studio 运行。
- 新的Android构建系统就是由Gradle的Android插件组成的

#### 新的Android构建系统特点

- 代码和资源易于重用
- 无论是针对多个 apk 发行版还是针对不同风格的应用程序，都可以很容易创建应用程序的多个不同版本
- 易于配置、扩展和自定义构建过程
- 良好的 IDE集成
- 
---

### AS的模块类型和项目视图

#### 模块类型

- Android Application Module
  - 构建系统会将其生成 Apk
- Android Library Module
  - 构建系统会将其生成 AAR
- App 引擎模块
- Java Library Module
  - 构建系统会将其生成 Jar

#### 项目视图
主要介绍项目的 build.gradle 和 模块的build.gradle

### 模块build.gradle

**Gradle的Android插件类型:**
- Application plugin:
  - plugin id: com.android.application
  - 会生成一个APK
- Library plugin:
  - plugin id: com.android.library
  - 会生成一个AAR，提供给其他应用程序模块用
- Test plugin:
  - plugin id: com.android.test
  - 用于测试其他的模块
- feature plugin:
  - plugin id: com.android.feature
  - 创建Android Instant App时需要用到的插件
- Instant App plugin: 
  - plugin id: com.android.instantapp
  - Android Instant App的入口

#### Application Plugin 

闭包 android 的属性(部分)

- minSdkVersion: App最低支持的SDK版本
- targetSdkVersion: 基于哪个SDK版本开发
- testApplicationId: 配置测试App的包名
- testInstrumentationRunner: 配置单元测试使用的Runner，默认为 android.test.InstrumentationTestRunner

buildTypes 块支持的属性
- applicationIdSuffix: 配置applicationIdSuffix 的后缀
- debuggable: 表示是否支持断点调试
- jniDebuggable: 是否可以调试NDK代码
- buildConfigField: 配置不同开发环境，比如测试环境和正式环境
- shrinkResources: 是否自动清理未使用的资源，默认 false
- zigAlignEnable: 是否开启zigalign优化，提高apk运行效率
- proguardFile: ProGuard混淆所用的ProGuard配置文件
- proguardFiles: 同时配置多个ProGuard配置文件
- signingConfig: 配置默认的签名信息
- multiDexEnable: 是否启用自动拆分多个Dex功能

signingConfigs块

- storeFile: 签名证书文件
- storePassword: 签名证书文件密码
- storeType:签名证书的类型
- keyAlias: 签名证书中密钥别名
- keyPassword: 签名证书中密钥的密码

其他配置快
- sourceSets: 配置目录指向
- productFlavors: 多个渠道配置
- lintOptions: Lint配置
- dexOptions: Dex工具配置
- adbOptions: adb配置
- packagingOptions: 打包时的相关配置

#### 全局配置
如果有多个module的配置一样，可以把配置提取出来，做为全局配置；有多种方式:

其中2种:
- [使用 ext 块配置](#ext-配置)
- [使用 config.gradle 配置](#使用-configgradle-配置)

##### ext 配置

```groovy
ext {
  a='xx'
  b='xx'
}

// 使用
android {
  compileSdkVersion rootProject.ext.a
  buildToolsVersion rootProject.ext.b
}
```

##### 使用 config.gradle 配置

step1: 项目根目录创建 config.gradle
step2: 项目根目录 build.gradle 
  - 新增代码: ``apply from: "config.gradle"``
step3: module 中的 build.gradle 使用
  - `rootProject.ext.android.applicationId`
  - `rootProject.ext.android.compileSdkVersion`
  - `rootProject.ext.android.buildToolVersion`

config.gradle 内容:
```groovy

ext {
  android=[
    applicationId:"xxx",
    compileSdkVersion:30,
    buildToolVersion: "30.0.0",
    minSdkVersion: 21,
    targetSdkVersion: 30
  ]
  
  dependencies=[
    "appcompt-v7":"com.android.suppor:appcompat-v7:28.0.0",
    "xx":"xxx"
  ]
}
```

### Android签名文件配置

项目大，团队人员多的时候，为了安全 签名配置不应该放在 build.gradle 中，如何解决签名配置问题？

method1: 自定义一个签名配置文件
method2: 本地~/.gradle/gradle.properties 文件中配置签名信息
method3: 放在打包服务器上

### Gradle的库依赖管理

#### 依赖传递

projectA 依赖 projectB，projectB 依赖 projectC，那么 projectA 就会依赖 projectC；

停止依赖传递，如下:
```groovy
implementation('xxx') {
  transitive false
}
```

#### 依赖检查

- 使用Gradle命令行
- 使用Gradle View 插件

#### 依赖冲突

- force
- exclude


##### force

```groovy
// 强制所有的库都用这个版本的 okio; 在某个 module 下的 build.gradle
configurations.all {
  resolutionStrategy {
    force 'com.squareup.okio:okio:2.1.0'
  }
}
```

##### exclude
```groovy
// 不再想依赖 com.android.support:support-nnotations
configurations {
  all*.exclude group: 'com.android.support', module: 'support-annotations'
}
```
