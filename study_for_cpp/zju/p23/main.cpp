#include <iostream>

using namespace std;

class XYPoints {};

class Shape {

 public:
  Shape();
  virtual ~Shape();
  virtual void render();
  void move(const XYPoints&);
  virtual void resize();

 protected:
  XYPoints center;
};

class Ellipse: public Shape {
 public:
  Ellipse(float maj, float minr);
  virtual void render();

 protected:
  float major_axis, minor_axis;
};

int main(){

  return 0;
}