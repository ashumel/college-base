#include <iostream>
#include <conio.h>
using namespace std;
int main() {
    const int n=10;
    int first=-1, last=-1, sum=0;
    int A[n];
    for (int i=0; i<n; i++){
    cin >> A[i];
        if (A[i]==0 && first==-1)
        first=i;
        if (A[i]==0 && i!=first)
        last=i; }
    if (first==-1 || last==-1)
        cout<< "Ошибка!";
    else {
        for (int i=first; i<=last; i++)
            sum+=A[i];
        cout<< "Сумма между первым и последним элементом равным 0: "<< sum; }
return 0; }