### 6.1 函数基础

[代码](../../chapter_6/section_1/6.1.cpp)

- [6.1.1 局部对象]
- [6.1.2 函数声明]
- [6.1.3 分离式编译]

#### 6.1.1 局部对象

- 自动对象(automatic object): 只存在与块执行期间的对象
- 局部静态对象(local static object): 直到程序终止才被销毁。

[练习代码](../../chapter_6/section_1/6.1.1.cpp)

#### 6.1.2 函数声明

函数声明三要素：返回值类型、函数名、参数类型。也称作 **函数原型**(function prototype)
```c++
int add(int a, int b);
```
和函数定义类似，不同的是，函数定义有函数体。

##### 在头文件中进行函数声明
[练习代码](../../chapter_6/section_1/6.1.2.cpp)

- 在头文件中声明
- 在源文件中定义

这样做能确保同一函数的所有声明保持一致，一旦要改变函数接口，只需改变一条声明即可。

##### 6.1.3 分离式编译(separate compilation)

允许把程序分隔到几个文件中，每个文件独立编译。

6.1.3 节练习：编译 [fact.cpp](../../chapter_6/section_1/fact.cpp) 和 [factMain.cpp](../../chapter_6/section_1/factMain.cpp)

**1. 编译加链接一起**
```shell
# 编译加链接一起，结果会生成 a.out ，执行 a.out 即可看到编译的程序
g++ fact.cpp factMain.cpp 
```

**2. 分离式编译**
```shell
# 编译 fact.cpp, 生成 fact.o
g++ -c fact.cpp

# 编译 factMain.cpp, 生成 factMain.o
g++ -c factMain.cpp

# 链接 fact.o 和 factMain.o，并且生成 main 的可执行文件
g++ fact.o factMain.o -o main
```
如果要修改文件，比如修改 fact.cpp，修改后，重新编译 fact.cpp，再链接 fact.o 和 factMain.o 即可。factMain.cpp 不需要再编译了。

