#include <iostream>

using namespace std;


class Sniper;
class Supplier;

class Supplier {
    int storage;

public:
    Supplier(int storage = 1000):storage(storage){

    }

    /**
     * 提供子弹；因为 Supplier 是 Sniper 的 friend class，因此可以访问 Sniper 的 private 的 member：bullets
     * @param sniper
     * @return
     */
    bool provide(Sniper &sniper);
};

class Sniper {
    int bullets;

public:
    Sniper(int bullets = 0): bullets(bullets){}
    friend bool Supplier::provide(Sniper & sniper);
};

bool Supplier::provide(Sniper &sniper){
    if (sniper.bullets < 20 ) { // 子弹少于 20 了
        if (this->storage > 100) {
            sniper.bullets += 100;
            this->storage -= 100;
        } else if(this->storage > 0){
            sniper.bullets += this->storage;
            this->storage = 0;
        } else {
            return false;
        }
    }
    cout << "sniper has " << sniper.bullets << " bullets now." << endl;
    return true;
}

int main(){

    Sniper sniper(2);
    Supplier supplier(2000);
    supplier.provide(sniper);

    return 0;
}