## typedef 关键词

[代码](../../c_from_hello_code/44_typedef/main.c)

- [不同平台](#不同平台)
- [定义别名](#定义别名)
- [用于 struct](#用于struct)
- [typedef 和 define 区别](#和define区别)
- [整型类型别名无需自己定义](#整型类型别名无需自己定义)
- [整型可移植性](#整型可移植性)

### 不同平台
不同平台整型对应的字节是不同的，如下:

**Visual Studio 2019**
- `int int32_t`
- `short int16_t`
- `char int8_t`

**其他平台**
- `long int32_t`: 4个字节
- `int16_t int int16_t`: 2个字节
- `char int8_t`: 1个字节

### 定义别名

```c
typedef int int32_t;
```

### 用于struct

结构类型别名为：person
```c
typedef struct {
  char name[];
  int gender;
} person;
```
使用结构时，不需要用 `struct` 关键词了，直接用 `person` 即可

### 和define区别

- `#define` 可以为值设置一个别名，`typedef` 不行
- `#define` 由预处理器处理，`typedef` 由编译器处理

### 整型类型别名无需自己定义

- 编译器会根据不同平台的整型范围大小，设置对应的别名。
- 引入头文件: `stdint.h` 就可以使用了

### 整型可移植性

- 引入头文件：`inttypes.h`
