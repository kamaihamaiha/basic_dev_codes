#include <iostream>

using namespace std;

class Mat {
public:
    enum DataType {
            TYPE8U,
            TYPE8S,
            TYPE32F,
            TYPE64F
    };
private:
    DataType type;
    void *data;
public:
    Mat(DataType type): type(type), data(NULL) {}
    DataType getType() const {
        return type;
    }
};

int main(){

    Mat image(Mat::DataType::TYPE8U);

    if (image.getType() == Mat::DataType::TYPE8U) {
        cout << "This is an 8U matrix." << endl;
    } else {
        cout << "I am not an 8U matrix." << endl;
    }

    return 0;
}