#include <iostream>
#include <memory>

using namespace std;

class MyTime {
    int hours;
    int minutes;
public:
    MyTime() : hours(0), minutes(0) {
        std::cout << "Constructor MyTime()" << std::endl;
    }

    MyTime(int m) : hours(0), minutes(m) {
        std::cout << "Constructor MyTime(int)" << std::endl;
        this->hours += this->minutes / 60;
        this->minutes %= 60;
    }

    MyTime(int h, int m) : hours(h), minutes(m) {
        std::cout << "Constructor MyTime(int,int)" << std::endl;
        this->hours += this->minutes / 60;
        this->minutes %= 60;
    }

    ~MyTime() {
        std::cout << "Destructor MyTime(). Bye!" << std::endl;
    }

    MyTime operator+(int m) const {
        MyTime sum;
        sum.minutes = this->minutes + m;
        sum.hours = this->hours;
        sum.hours += sum.minutes / 60;
        sum.minutes %= 60;
        return sum;
    }

    friend std::ostream &operator<<(std::ostream &os, const MyTime &t) {
        std::string str = std::to_string(t.hours) + " hours and "
                          + std::to_string(t.minutes) + " minutes.";
        os << str;
        return os;
    }
};

int main(){

    unique_ptr<MyTime> mt1(new MyTime(10));
    unique_ptr<MyTime> mt2 = make_unique<MyTime>(80); //C++17

    cout << "mt1: " << *mt1 << endl;
    cout << "mt2: " << *mt2 << endl;

//    unique_ptr<MyTime> mt3 = mt1; // error
    unique_ptr<MyTime> mt3 = move(mt1);
//    cout << "mt1: " << *mt1 << endl; // error
    cout << "mt3: " << *mt3 << endl;

}