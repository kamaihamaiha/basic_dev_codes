#include <iostream>

using namespace std;

struct Point{
    float x;
    float y;
};

template<typename T>
T sum(T x, T y) {
    cout << "The input type is: " << typeid(T).name() << endl;
    return x + y;
}

// Explicitly instantiate
template double sum<double>(double, double );

// specialization
template<> Point sum<Point>(Point p1, Point p2){
    cout << "The input type is: " << typeid(p1).name() << endl;
    Point p;
    p.x = p1.x + p2.x;
    p.y = p1.y + p2.y;
    return p;
}

int main(){

    // 显式实例化
    auto ret1 = sum(1, 2);
    auto ret2 = sum(1.0, 2.0);
    auto ret3 = sum(1.0f, 2.0f);

    // 隐式实例化
    auto ret4 = sum<int>(1.0, 2);

    // 特例模板使用
    Point p1 = {1, 2};
    Point p2 = {100, 200};
    Point pS = sum(p1, p2);
    cout << "pS: (" << pS.x << ", " << pS.y << ")" << endl;

    return 0;
}