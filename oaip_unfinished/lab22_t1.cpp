#include <iostream>
using namespace std;

class train {
    private:
    int number_example;
    string name_example;
    string time1_example;
    string time2_example;
    public:
        train(int number_example, string name_example, string time1_example, string time2_example) {
            this->number_example = number_example;
            this->name_example = number_example;
            this->time1_example = number_example;
            this->time2_example = number_example;
        } void setTrain() {
            cout << "Номер поезда: \n";
            cin >> number_example;
            cout << "Имя поезда: \n";
            cin >> name_example; 
            cout << "Время отправления: \n";
            cin >> time1_example;
            cout << "Время прибытия: \n";
            cin >> time2_example;
        } void getTrain() {
            cout << "number = " << number_example << endl;
            cout << "name = " << name_example << endl;
            cout << "time1 = " << time1_example << endl;
            cout << "time2 = " << time2_example << endl;
        } ~train() {
            cout << "Сработал деструктор:)" << endl;
        }
};

int main() {
    for(int i = 0; i < 3; i++) {
    train obj1(1, "BG-450", "15:40", "17:10");
    obj1.setTrain();
    obj1.getTrain();
    }
}