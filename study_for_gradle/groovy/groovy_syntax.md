## Groovy 语法

源自Java 语法

基于JVM的面向对象编程语言，既可以面向对象编程，也可以用作纯粹的脚本语言；语言上吸纳了Python、Ruby和Smalltalk语言的优秀特性；比如
动态类型转换、闭包和元编程支持


### Groovy的编写和调试

- 在 Android Studio 和 IntelliJ IDEA 可以
- 或者文本编辑器，如: Sublime Text

### 特点

#### 方法
- def 关键字定义方法
- 如果有指定返回值类型，可以不加 def
- 参数类型可以忽略
- return 可以忽略
- 调用方法时，() 可以忽略

#### 类
- 字段自动生成 getter和setter方法
- 类不用和源文件相同名称

#### 断言

一直处于开启状态（和Java 不同），是进行单元测试的首选方式

#### for 循环

1. 支持 ``for(int i = 0; i < 10; i++)`` 和 ``for(int i: values)``
2. 支持 for in loop 形式: ``for (i in 0..9)``
3. 支持遍历列表: ``for (i in [0, 1, 2, 3])``
4. 遍历Map的值: 
    ```
    def map = ['a': 1, 'b': 2, 'c':3]
    for( v in map.values() ) {
        ...
    }
    ```
#### switch 语句

允许的类型

- string
- list
- range
- Type

#### 字符串

- 单引号
- 双引号: 支持插值
- 三引号: 输出后，会保留格式（换行，缩进格式）

##### GString

- 是可变的

#### List

见 [build.gradle task testList](./demo/build.gradle)

#### Map
见 [build.gradle task testMap](./demo/build.gradle)


#### 闭包
见 [build.gradle task testClosure](./demo/build.gradle)

定义格式
```groovy
def closure = { [ closureParameters -> ] statements }

// 只有一个参数
def closure {
    param -> println param
}

// 等价于
def closure {
    it -> println it
}

// 等价于
def closure {
    println it
}

// 调用，多种方式
closure("hello")
closure.call("hello-call")
clousre 'hello...'
```

#### IO操作
见 [build.gradle task testIO](./demo/build.gradle)

#### asType

可以用作类型转换

#### 判断是否为真

```java
// Java 中这么判断
String name;
if(name != null && name.length > 0)

// groovy 中这么判断
if(name)
```

#### 判空

像 Kotlin
```groovy
println school?.student?.name
```

#### with 操作符
像 Kotlin，略
