### 定义和初始化 vector 对象

几种初始化 vector 对象方式：
```c++
vector<T> v1;                 // v1 是一个空 vector，它潜在的元素是 T 类型，执行默认初始化
vector<T> v2(v1);             // v2 中包含 v1 所有元素副本
vector<T> v3 = v1;            // 同上
vector<T> v4(n, val);         // v4 中包含 n 个重复元素，每一个元素的值都是 val
vector<T> v5{a, b, c...};     // v5 包含 a,b,c... 元素
vector<T> v6 = {a, b, c...};  // 同上
```

#### 列表初始化 vector 对象
```c++
vector<string> articles = {"a", "an", "the"};
// 或者
vector<string> v1{"a", "b", "c"};
```

#### 创建指定数量的元素
```c++
vector<int> ivec(10, 8);          // 10 个元素，每个元素初始值都为 8
vector<string> svec(10, "hello")  //10 个元素，每个元素初始值都为 hello
```

#### 值初始化
只提供元素数量，而省略初始值。库会创建一个**值初始化**(value-initialized)元素初值，并赋给容器中的所有元素。
```c++
vector<int> ivec(10);     // 10 个元素，每个元素初始值都为 0
vector<string> svec(10);  // 10 个元素，每个元素初始值都为 空string对象
```

#### 列表初始值还是元素数量？
```c++
vector<int> v1(10);     // 10 个元素，每个元素都是 0
vector<int> v2{10};     // 一个元素：10
vector<int> v3(10, 1);  // 10 个元素，每个元素都是 1
vector<int> v4{10, 1};  // 2 个元素：10 和 1
```

另外一种情况：使用了 `{}` 初始化，但是提供的值不能用来列表初始化，就要考虑用这样的值来构造 vector 对象：
```c++
vector<string> v1{"hi"};      // 有一个元素
vector<string> v2("hi");      // error: 不能使用字符串字面值构建 vector 对象
vector<string> v3{10};        // 10 个默认初始化的元素
vector<string> v4{10, "hi"};  // 10 个值为 "hi" 的元素
```