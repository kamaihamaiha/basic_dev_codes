#include <iostream>
#include <cstdlib>
#include <cfloat>
#include <cmath>

float radio(float a, float b){
    if (fabs(a + b) < FLT_EPSILON) {
        // 抛出异常
        throw "The sum of the two arguments is close to zero.";
    }
    return ((a - b) / (a + b));
}

int main(){

    float x = 0.f;
    float y = 0.f;
    float z = 0.f;

    std::cout << "Please input two numbers <q to quit>:";

    while (std::cin >> x >> y) {

        try {
            z = radio(x, y);
            std::cout << "radio(" << x << ", " << y << ") = " << z << std::endl;
        } catch (const char *msg){
            std::cerr << "Call ratio() failed: " << msg << std::endl;
            std::cerr << "I give you another chance." << std::endl;
        }


        std::cout << "Please input two numbers <q to quit>:";
    }
    std::cout << "Bye!" << std::endl;
    return 0;
}