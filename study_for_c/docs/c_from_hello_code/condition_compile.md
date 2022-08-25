## 条件编译

- 用到预处理指令 `#if`
- 格式：`#if 常量表达式`
- 用 `#endif` 标记结束
- 在编译前，由预处理器处理
    - 根据分支走向，保留需要走向分支的代码，删除被跳过分支的代码
    
### 使用举例

- [`#if xxx`](#情况1)
- [`#if xxx` `#else`](#情况2)
- [`#if xxx` `#elif` `#else`](#情况3)
- [`#ifdef` & `#ifndef`](#情况4)

#### 情况1
`#if xxx `   
`#endif`   
预处理前：
```c
#define N 0
    
    int main(){
      #if N == 1
        printf("1");
      #endif
        printf("A");
      return 0;
    }
```

预处理后(N 为 0 时)：
```c
    int main(){
      printf("A");
      return 0;
    }
```
预处理后(N 为 1 时)：
```c
    int main(){
        printf("1");
        printf("A");
      return 0;
    }
```

#### 情况2

`#if xxx`  
`#else`  
`#endif`

处理前：
```c
#define N 0

int main(){
  #if N == 1
    printf("1");
  #else
    printf("A");
  #endif  
  return 0;
}
```

处理后(N = 0)：
```c
int main(){
    printf("A");
  return 0;
}
```

处理后(N = 1)：
```c
int main(){
    printf("1");
  return 0;
}
```

#### 情况3

`#if xxx`  
`#elif xxx`  
`#else`  
`#endif`

#### 情况4
测试宏是否被定义过：
- `#ifdef`: if defined
  - `#ifdef 宏` 可以用 `#if defined(宏)` 替代
- `#ifndef`: if not defined


##### `#if defined(宏)` 和 `#elif defined(宏)`

```c
#define PN

int main(){
  #if defined(PN)
    printf("1");
  #elif defined(PN)
    printf("A");
  #else
    printf("*");
  #endif  
  return 0;
}
```
