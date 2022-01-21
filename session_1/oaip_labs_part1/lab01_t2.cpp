#include <iostream>
using namespace std;

int main(){
    setlocale(LC_ALL, "rus");
    int num;
    cout <<"Введите четырехзначное число: ";
    cin>> num;
    cout << "Цифры в обратном порядке: ";
    cout << num % 10;
    num /= 10; 
    cout << num % 10; 
    num /= 10;
    cout << num % 10;
    num /= 10;
    cout << num % 10;
    num /= 10;
    cout << endl;
return 0; }