//Feito com Jvdroid

import java.util.Scanner;

public class DesafiosExtrasScanner {
    public static void main(String[] args) {
        
        // Criar objeto para coleta de entradas
        Scanner scanner = new Scanner(System.in);
    
        // Obter nome do usuário
        System.out.println("Digite seu nome: ");
        String nome = scanner.nextLine();
    
        // Obter idade do usuário
        System.out.println("Digite sua idade: ");
        int idade = scanner.nextInt();
        
        // Obter Peso
        System.out.println("Digite seu peso: ");
        float peso = scanner.nextFloat();
        
        // Obter Altura
        System.out.println("Digite sua altura: ");
        float altura = scanner.nextFloat();
    
        // Exibir resultados
        System.out.printf("Bem-vindo, %s!\n", nome);
    
        if (idade >= 18) {
            System.out.printf("Você é maior de idade, tem %d anos.\n", idade);
        } else {
            System.out.printf("Você é menor de idade, tem %d anos.\n", idade);
        }
        
        System.out.printf("Você pesa %.2f kilos", peso );
        
        System.out.printf("\nVoce tem %.2f de altura.", altura);
        
        scanner.close();
        
    }
}