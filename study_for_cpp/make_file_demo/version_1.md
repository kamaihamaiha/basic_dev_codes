## Makefile 版本1

### 最简单的 Makefile 脚本

- 缺点是每次编译都会编译全部 cpp 文件
```makefile
hello: main.cpp sayHello.cpp factorial.cpp
	g++ -o hello main.cpp sayHello.cpp factorial.cpp
```

- 第一行解读
    - hello 是目标
    - 后面的三个 cpp 文件是依赖
- 第二行解读
    - 实现目标 hello 的命令
    - 一定要用 tab 键空出来

#### 使用 make 命令，执行 Makefile

- 在当前目录下执行 make 命令，make 就会找当前目录下名为 Makefile 的文件
- 如果名字不是 Makefile，则可以指定文件：``make -f 你的文件名`

运行如下：
```shell
kk@192 make_file_demo % ./hello 
Hello!
This is main:
The factorial of 5 is: 120
```
如果再次执行 make，则会提示如下：
```shell
kk@192 make_file_demo % make
make: `hello' is up to date.
```
##### 说明：
- Makefile 判断 hello 是最新的（相比于他的依赖：三个 cpp文件），因此不会再执行后面的 g++ -o xxx 命令了
- 此时如果，去修改 cpp 文件，然后再执行 cmake，又会重新执行后面的命令了