#include <iostream>
#include <string>
using namespace std;
int main() {
    int MAX = 256;
    char str1[MAX], symbol1, symbolreplace1 = '*';
    cout << "Введите строку: ";
    cin.get(str1, MAX);
    cout << "Символ который хотите заменить на '*': "; 
    cin >> symbol1;
    for (int i = 0; str1[i]; i++) {
        if(str1[i] == symbol1) str1[i] = symbolreplace1; }
    cout << str1 << endl;
    cin.ignore();
    string str2 = "Hello, World!", symbol2, symbolreplace2 = "*";
    cout << "Символ который хотите заменить на '*': ";
    getline(cin, symbol2);
    for (int i = 0; i < 2; i++ ) {
        str2.replace(str2.find(symbol2), 1, symbolreplace2);
    } cout << str2 << endl;
return 0; }