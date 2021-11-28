#include <iostream>
using namespace std;

double recursia(int sum, int count) {
    int number;
    cin >> number;
    if (!number) 
    return (double) sum/count;
    return recursia(sum + number, count+1);
} int main() {
    cout << recursia(0, 0);
}