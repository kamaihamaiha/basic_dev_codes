#include <iostream>

using namespace std;

// class template
template<typename T, size_t rows, size_t cols>
class Mat {
    T data[rows][cols];
public:
    Mat(){}
    /**
     * the default copy constructor will copy each element of a static array member
     * so we don't 'delete' the copy constructor
     * the same with the assignment operator
     * Mat(const Mat&) = delete;
     * Mat& operator=(const Mat&) = delete;
     */
     T getElement(size_t r, size_t c);
     bool setElement(size_t r, size_t c, T value);
};

template<typename T, size_t rows, size_t cols>
T Mat<T, rows, cols>::getElement(size_t r, size_t c) {
    if (r >= rows || c >= cols){
        cerr << "getElement(): indices are out of range" << endl;
        return 0; // 返回值要求是 T，为什么这里可以返回 0 ？
        // 问了 chatGPT：这里返回的是一个T类型的变量，而0是T类型的默认值，可以被隐式转换为T类型的变量并返回。
    }
    return data[r][c];
}

template<typename T, size_t rows, size_t cols>
bool Mat<T, rows, cols>::setElement(size_t r, size_t c, T value) {
    if (r >= rows || c >= cols){
        cerr << "setElement(): indices are out of range" << endl;
        return false;
    }
    data[r][c] = value;
    return true;
}

// 显示初始化模板 Mat<int, 2, 2>
template class Mat<int, 2, 2>;

typedef Mat<int, 2, 2> Mat22i; // 使用时直接用 Mat22i 就可以

int main(){

    Mat22i mat;
    mat.setElement(2, 2, 256);
    cout << mat.getElement(2, 2) << endl;

    mat.setElement(1, 1, 256);
    cout << mat.getElement(1, 1) << endl;

    Mat<float, 3, 1> vec;
    vec.setElement(2, 0, 3.14f);
    cout << vec.getElement(2, 0) << endl;

    Mat<float, 3, 1> vec2(vec); // 使用了 copy constructor
    cout << vec2.getElement(2, 0) << endl;


    return 0;
}