#include <iostream>
#include <string>

using namespace std;


class Area {
 private:
  int size;         // 面积
  string location;  // 坐标位置

 public:
  Area(int size, string loc): size(size), location(loc) {

  }
  ~Area(){}

  int getSize(){
    return size;
  }

  string getLocation(){
    return location;
  }
};

class People {
 private:
  int population; // 人口
  string race;    // 民族

 public:
  People(int pop, string race): population(pop), race(race){}
  ~People(){}

  int getPop(){
    return population;
  }

  string getRace(){
    return race;
  }
};


// 国家由 国土和人口组成
class Country {
 private:
  Area area;
  People people;

 public:
  Country(int size, string location, int pop, string race): area(size, location), people(pop, race) {

  }
  ~Country(){}

  Area getArea(){
    return area;
  }

  People getPeople(){
    return people;
  }
};


int main(){

  Country *country = new Country(960, "东方", 14000, "汉族");

  cout << "country info: " << country->getArea().getLocation() << ", " << country->getArea().getSize() << ", " << country->getPeople().getPop() << ", " << country->getPeople().getRace() << endl;

  return 0;
}