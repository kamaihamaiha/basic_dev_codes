#include <iostream>

using namespace std;

// Class Template: 定义类模板
template<typename T>
class Mat {
    size_t rows;
    size_t cols;
    T * data;
public:
    Mat(size_t rows, size_t cols):rows(rows), cols(cols){
        data = new T[rows * cols * sizeof(T)];
    }
    ~Mat(){
        delete[] data;
    }

    T getElement(size_t r, size_t c);
    bool setElement(size_t r, size_t c, T value);
};

template <typename T>
T Mat<T>::getElement(size_t r, size_t c) {
    if (r >= this->rows || c >= this->cols) {
        cerr << "getElement(): Indices are out of range" << endl;
        return 0;
    }
    return this->data[cols * r + c];
}

template <typename T>
bool Mat<T>::setElement(size_t r, size_t c, T value) {
    if (r >= this->rows || c >= this->cols) {
        cerr << "setElement(): Indices are out of range" << endl;
        return false;
    }
    data[this->cols * r + c] = value;
    return true;
}


// Explicitly instantiate
template class Mat<int>;

// 注意编译时要指定 c++11 标准: `g++ Mat.cpp --std=c++11 && ./a.out`
int main(){

    Mat<int> i_mat(3, 4);
    i_mat.setElement(1, 2, 256);

    Mat<float> f_mat(2, 3);
    f_mat.setElement(1, 2, 3.14159f);

    Mat<double> d_mat(2, 3);
    d_mat.setElement(1, 2, 2.718281828);

    // get element
    cout << i_mat.getElement(1, 2) << endl;
    cout << f_mat.getElement(1, 2) << endl;
    cout << d_mat.getElement(1, 2) << endl;
    return 0;
}