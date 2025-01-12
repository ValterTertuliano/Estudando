#include <iostream>
#include <windows.h> // para UTF-8

using namespace std;

int main(){
    // configura o console para utf-8
    SetConsoleOutputCP(CP_UTF8);
    int x;
    int y;
    int total;

    cout << "Digite um numero: ";
    cin >> x;

    cout << "Digite outro numero: ";
    cin >> y;

    total = x + y;

    cout << "\nA soma de " << x << " + " << y << " é " << total << endl;

    return 0;
}