#include <iostream>

using namespace std;

class MyTime{
private:
    int minutes;
    int hours;

public:
    MyTime():minutes(0),hours(0){}
    MyTime(int h, int m):minutes(m), hours(h){}

    // prefix increment: ++i
    MyTime& operator++(){
        this->minutes++;
        this->hours += this->minutes / 60;
        this->minutes = this->minutes % 60;
        return *this;
    }

    // postfix decrement: i++
    MyTime operator++(int){
        MyTime old = *this;
        operator++();
        return old;
    }

    string getTime() const {
        return to_string(this->hours) + " hours and " + to_string(this->minutes) + " minutes.";
    }
};

// 自增自减操作符重载
int main(){

    MyTime t1(1, 59);
    MyTime t2 = t1++;
    MyTime t3 = ++t1;

    cout << t1.getTime() << endl;
    cout << t2.getTime() << endl;
    cout << t3.getTime() << endl;
}