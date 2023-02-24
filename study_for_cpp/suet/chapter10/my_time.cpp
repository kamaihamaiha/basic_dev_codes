#include <iostream>

using namespace std;

class MyTime{
private:
    int minutes;
    int hours;

public:
    MyTime():minutes(0),hours(0){}
    MyTime(int h, int m):minutes(m), hours(h){}

    MyTime operator+(const MyTime &time) const {
        MyTime targetTime;
        targetTime.minutes = minutes + time.minutes;
        targetTime.hours = hours + time.hours;
        targetTime.hours += minutes / 60;
        targetTime.minutes %= 60;
        return targetTime;
    }

    MyTime operator+=(const MyTime &time) {
        this->minutes += time.minutes;
        this->hours += time.hours;
        this->hours += minutes / 60;
        this->minutes %= 60;
        return *this;
    }

    MyTime operator-(const MyTime &time) const {
        MyTime targetTime;
        targetTime.minutes = minutes - time.minutes;
        targetTime.hours = hours - time.hours;
        targetTime.hours += minutes / 60;
        targetTime.minutes %= 60;
        return targetTime;
    }

    MyTime operator-=(const MyTime &time) {
        this->minutes -= time.minutes;
        this->hours -= time.hours;
        this->hours += minutes / 60;
        this->minutes %= 60;
        return *this;
    }

    string getTime() const {
        return to_string(this->hours) + " hours and " + to_string(this->minutes) + " minutes.";
    }
};

int main(){

    MyTime t1(1, 10);
    MyTime t2(2, 20);

    cout << (t1 + t2).getTime() << endl;
//    cout << (t1 += t2).getTime() << endl;

    cout << (t2 - t1).getTime() << endl;


    return 0;
}