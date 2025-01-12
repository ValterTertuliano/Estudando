#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
#include <regex>
#include <windows.h>

using namespace std;

int main() {
    SetConsoleOutputCP(CP_UTF8);
    
    // Entrada do usuário
    cout << "Digite algo: ";
    string str;
    getline(cin, str); // outra forma de ler entradas do usuario

    // Verificar se é número
    bool isNumber = regex_match(str, regex("\\d+"));

    // Verificar se é letra
    bool isAlphabet = regex_match(str, regex("[a-zA-Z]+"));

    // Verificar se é alfanumérico
    bool isAlphanumeric = regex_match(str, regex("[a-zA-Z0-9]+"));

    // Verificar se é decimal
    bool isDecimal = regex_match(str, regex("\\d+(\\.\\d+)?"));

    // Verificar se está em maiúsculas
    string upperStr = str;
    transform(upperStr.begin(), upperStr.end(), upperStr.begin(), ::toupper);
    bool isUpperCase = (str == upperStr);

    // Verificar se está em minúsculas
    string lowerStr = str;
    transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);
    bool isLowerCase = (str == lowerStr);

    // Verificar se contém apenas espaços em branco
    bool isWhitespace = all_of(str.begin(), str.end(), ::isspace);

    // Resultados
    cout << "String original: " << str << endl;
    cout << "String em maiúsculas: " << upperStr << endl;
    cout << "É número? " << (isNumber ? "Sim" : "Não") << endl;
    cout << "É letra? " << (isAlphabet ? "Sim" : "Não") << endl;
    cout << "É alfanumérico? " << (isAlphanumeric ? "Sim" : "Não") << endl;
    cout << "É decimal? " << (isDecimal ? "Sim" : "Não") << endl;
    cout << "Está em maiúsculas? " << (isUpperCase ? "Sim" : "Não") << endl;
    cout << "Está em minúsculas? " << (isLowerCase ? "Sim" : "Não") << endl;
    cout << "Contém apenas espaços em branco? " << (isWhitespace ? "Sim" : "Não") << endl;

    return 0;
}
