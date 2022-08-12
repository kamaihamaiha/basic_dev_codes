#include <iostream>

using namespace std;

/*
* 一圆型游泳池如图所示，现在需在其周围建一圆型过道，并在其四周围上栅栏。栅栏价格为35元/米，过道造价为20元/平方米。
* 过道宽度为3米，游泳池半径由键盘输入。要求编程计算并输出过道和栅栏的造价。
* 图形描述：大圆嵌套小圆：
* 小圆在大圆中间，小圆为游泳池，大圆与小圆间隔为过道。
*/

const float PI = 3.14159;
const float BAR_PRICE = 35.0; //栅栏价格
const float PATH_PRICE = 20.0;//过道价格
const float PATH_WIDTH = 3.0; //过道宽度

class Circle {
private: float radius;
public:
    Circle(float radius);


    // 周长
    float circumference() const;

    // 面积
    float area() const;
};


// 实现 Circle 的方法
Circle::Circle(float radius) {
    this->radius = radius;
}

// 计算圆的周长
float Circle::circumference() const {
    return radius * 2 * PI;
}

// 计算圆的面积
float Circle::area() const {
    return PI * radius * radius;
}


int main() {

    float radius1, radius2;
    float pathCost; // 过道造价
    float barCost; // 栅栏造价

    Circle *pool = NULL;
    Circle *yard = NULL;


    // 过道面积：大圆面积 - 小圆面积

    // 提示用户输入半径
    cout << "请输入泳池的半径: ";
    cin >> radius1;

    radius2 = radius1 + PATH_WIDTH;

    pool = new Circle(radius1);
    yard = new Circle(radius2);

    // 计算过道造价
    pathCost = (yard->area() - pool->area()) * PATH_PRICE;

    // 计算栅栏造价
    barCost = yard->circumference() * BAR_PRICE;

    // 输出
    cout << "过道造价: " << pathCost << "¥" << endl;
    cout << "栅栏造价: " << barCost << "¥" << endl;

    delete pool;
    delete yard;

    return 0;
}