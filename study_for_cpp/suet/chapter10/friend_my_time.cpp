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

    // MyTime + Int 需要根据自己的需要定制
    MyTime operator+(int num) const{
        MyTime time;
        time.minutes = this->minutes + num;
        time.hours = this->hours;
        time.hours += time.minutes / 60;
        time.minutes = time.minutes % 60;
        return time;
    }

    friend MyTime operator+(int m, const MyTime &time) {
        return time + m;
    }

    // << 也可以重载
    friend std::ostream & operator<<(std::ostream &os, const MyTime &time){
        string info = to_string(time.hours) + " hours and " + to_string(time.minutes) + " minutes.";
        os << info;
        return os;
    }

    // >> 也可以重载
    friend std::istream & operator>>(std::istream &is, MyTime &time){
        is >> time.hours >> time.minutes;
        time.hours += time.minutes / 60;
        time.minutes %= 60;
        return is;
    }

    string getTime() const {
        return to_string(this->hours) + " hours and " + to_string(this->minutes) + " minutes.";
    }
};




int main(){

    MyTime t1(1, 10);
    cout << (t1 + 8).getTime() << endl;

    cout << (10 + t1).getTime() << endl;

    // 这个调用的是 << 运算符的重载
    cout << t1  << endl;

    cout << "Please input two integer numbs: " << endl;
    cin >> t1;
    cout << t1 << endl;

    return 0;
}