## 在独立项目中创建自定义插件

- [引入 groovy 语法和 Gradle api](./build.gradle)
- [编写自定义插件 HumanPlugin](src/main/groovy/cn.kk.plugins/HumanPlugin.groovy)
- 创建插件配置文件
- 上传插件

### 创建插件配置文件

- 在 src/main/resources 新建 `META-INF/gradle-plugins` 目录
- 创建配置文件: ``cn.kk.plugins.HumanPlugin.properties``
  - 格式: plugin_id.plugin_name.properties

### 上传插件

见 [build.gradle](./build.gradle)

得到的插件位置: [../repo/cn/kk/plugins/GradlePluginShare/0.9.9/GradlePluginShare-0.9.9.jar](../repo/cn/kk/plugins/GradlePluginShare/0.9.9/GradlePluginShare-0.9.9.jar)