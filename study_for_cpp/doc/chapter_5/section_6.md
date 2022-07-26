### try 语句块和异常处理
[代码](../../chapter_5/5.6.cpp)   

标准库中定义了一组类，用于报告标准库函数遇到的问题，分别定义在 4 个头文件中：
- `exception`: 定义了最通用的异常类 `exception`
- `stdexcept`: 定义了几种常见的异常类，见：表5.1
- `new`: 定义了 `bad_alloc` 异常类型
- `type_info`: 定义了 `bad_cast` 异常类型