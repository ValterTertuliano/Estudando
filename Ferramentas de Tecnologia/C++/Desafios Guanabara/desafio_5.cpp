#include <iostream>
#include <windows.h>

using namespace std;

int main(){

    SetConsoleOutputCP(CP_UTF8);

    int num;

    cout << "Digite um número: ";
    cin >> num;

    int sucessor = num + 1;
    cout << "Sucessor: " << sucessor;

    int antecessor = num - 1;
    cout << "\nAntecessor: " << antecessor;

    return 0;
}