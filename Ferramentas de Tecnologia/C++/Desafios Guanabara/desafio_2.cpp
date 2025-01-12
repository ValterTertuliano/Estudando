#include <iostream>

int main(){
    std::string nome; // variavel para receber nome do usuario

    std::cout << "Digite seu nome: ";
    std::cin >> nome; // obtem o nome até o primeiro espaço em branco
    std::cout << "Seja bem vindo " << nome << "\n";
    return 0;
    
}