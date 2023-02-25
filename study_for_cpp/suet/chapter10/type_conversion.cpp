#include <iostream>

using namespace std;

class MyTime{
private:
    int hours;
    int minutes;

public:
    MyTime():hours(0),minutes(0){}

    // int => MyTime
    MyTime(int m):hours(0),minutes(m){
        this->hours += this->minutes / 60;
        this->minutes = this->minutes % 60;
        cout << "Constructor MyTime()" << endl;
    }

    MyTime operator=(int m){ // 直接用 int 给 MyTime 赋值
        this->minutes = m;
        this->hours = this->minutes / 60;
        this->minutes = this->minutes % 60;
        cout << "MyTime = " << endl;
        return *this;
    }

    // MyTime => int
    operator int() const {
        return this->hours * 60 + this->minutes;
    }
    // MyTime => float
    explicit operator float() const {
        return float(this->hours * 60 + this->minutes);
    }

    string getTime() const {
        return to_string(this->hours) + " hours and " + to_string(this->minutes) + " minutes.";
    }
};

int main(){

    // int => MyTime
    MyTime t1 = 100;
    cout << t1.getTime() <<  endl;

    t1 = 130;
    cout << t1.getTime() << endl;

    // MyTime => int
    int t1ValueI = t1;
    float t1ValueF = float(t1); // 因为定义运算符的时候为显示转换，所以加了 float()

    cout << "t1ValueI: " << t1ValueI << endl;
    cout << "t1ValueF: " + to_string(t1ValueF) << endl;
    return 0;
}