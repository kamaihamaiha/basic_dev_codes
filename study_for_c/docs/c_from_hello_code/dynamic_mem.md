## 动态内存管理
[代码](../../c_from_hello_code/53_dynamic_mem/main.c)

- 变长数组
    - 不建议使用，已经从 C语言编译器移除
- `void* malloc(size_t size)` 函数，在 `stdlib.h` 中
    - 从内存中申请一组连续的内存空间
    - size: 需要申请的内存空间大小
    - 返回值: 申请成功，则返回成功申请的内存首地址；申请失败，返回 NULL
- 释放内存空间
    - `void free(void* ptr);`
    
    
- `void*` 
  - C语言可以通过赋值转换为其他类型的指针
  - C++ 必须强制转换后，才可以赋值给其他类型的指针
  - 为了代码可移植性，建议都是用强制转换  
    
- 通过 `malloc()` 得到的指针，可以作为函数的返回值
    

