import java.util.Scanner;

public class desafio_1 {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite seu Nome: ");
        String entrada = scanner.nextLine();
        
        System.out.println("Olá, " + entrada + "! Prazer em te conhecer!");

        scanner.close();
    }
}
