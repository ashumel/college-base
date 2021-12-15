#include "lab24_t1_func.cpp"

int main() {
    double a = 0.2;
    double b = 1;
    int n = 10;
    cout << "Метод левых прямоугольники: " << leftpraym(a, b, n) << endl;
    cout << "Метод правых прямоугольники: " << rightparam(a, b, n) << endl;
    cout << "Метод трапеции: " << trapec(a, b, n) << endl;
    cout << "calceValue: " << calceValue(a, b, n) << endl;
    cout << "primitive: "  << primitive(a, b, n) << endl;
return 0; }