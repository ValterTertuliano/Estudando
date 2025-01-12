// Faça um programa que peça um numero e informe seu sucessor e antecessor

import java.util.Scanner;
public class desafio_5 {

    public static void main(String[] args) {
        int antecessor, sucessor;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int num = scanner.nextInt();
        
        antecessor = num - 1;
        System.out.println("Seu ANTECESSOR é: " + antecessor);

        sucessor = num + 1;
        System.out.println("Seu SUCESSOR é: " + sucessor);

        scanner.close();
        
    }
}