#include <iostream>

using namespace std;

// 定义类模板：MyVector
template<typename T>
class MyVector{
    size_t length;
    T *data;

public:
    MyVector(size_t length):length(length){
        data = new T[length * sizeof(T)]{};
    }
    ~MyVector(){
        delete [] data;
    }

    MyVector(const MyVector&) = delete; // 表示禁用了拷贝构造函数
    MyVector& operator=(const MyVector&) = delete;

    T getElement(size_t index);
    bool setElement(size_t index, T value);
};

// region 实现类模板 MyVector 的方法:
// getElement()

template<typename T>
T MyVector<T>::getElement(size_t index) {
    if (index >= this->length){
        cerr << "getElement(): Indices are out of range" << endl;
        return 0;
    }
    return data[index];
}

template<typename T>
bool MyVector<T>::setElement(size_t index, T value) {
    if (index >= this->length){
        cerr << "getElement(): Indices are out of range" << endl;
        return false;
    }
    data[index] = value;
    return true;
}

// 对 bool 类型的 vector 进行特化
template<>
class MyVector<bool> {
    size_t length;
    unsigned char *data;

public:
    MyVector(size_t length):length(length){
        // 需要的字节数计算: 因为用一个 byte 表示一个 bool 太浪费
        int num_bytes = (length - 1) / 8 + 1;
        data = new unsigned char[num_bytes]{};
    }
    MyVector(const MyVector&) = delete; // 表示禁用了拷贝构造函数
    MyVector& operator=(const MyVector&) = delete;
    bool getElement(size_t index);
    bool setElement(size_t index, bool value);
};


bool MyVector<bool>::getElement(size_t index) {
    if (index >= this->length){
        cerr << "getElement(): Indices are out of range" << endl;
        return 0;
    }
    // 这个代码细节，要自己理一理
    size_t byte_id = index / 8;
    size_t bit_id = index % 8;
    unsigned char mask = (1 << bit_id);
    return bool(data[byte_id] & mask);
}

bool MyVector<bool>::setElement(size_t index, bool value) {
    if (index >= this->length){
        cerr << "getElement(): Indices are out of range" << endl;
        return false;
    }
    size_t byte_id = index / 8;
    size_t bit_id = index % 8;
    unsigned char mask = (1 << bit_id);
    if (value){
        data[byte_id] |= mask;
    } else {
        data[byte_id] &= ~mask;
    }
    return true;
}

// endregion

int main(){

    MyVector<int> vec_i(16);
    vec_i.setElement(3, 256);
    cout << vec_i.getElement(3) << endl;

    MyVector<bool> vec_b(17);
    vec_b.setElement(15, false);
    vec_b.setElement(16, true);
    cout << vec_b.getElement(15) << endl;
    cout << vec_b.getElement(16) << endl;

    return 0;
}