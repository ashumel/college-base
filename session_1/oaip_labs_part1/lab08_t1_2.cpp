#include <iostream>
using namespace std;
int main() {
    setlocale(LC_ALL,"rus");
    int MAX = 60;
    char str1[MAX], str2[MAX];
    cout << "Введите две строки для комбинации: ";
    gets(str2);
    gets(str1);
    char *to = str2, *from = str1;
    while(*to) to++;
    while(*from) {
        *to = *from;
        to++;
        from++; }
    cout << "Скомбинированная строка: " << str2; 
    return 0; }