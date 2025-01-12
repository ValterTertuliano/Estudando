import java.util.Scanner;

public class desafio_4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Entrada do usuário
        System.out.print("Digite algo: ");
        String str = scanner.nextLine();

        // Verificações diretamente no método main
        System.out.println("String original: " + str);
        System.out.println("String em maiúsculas: " + str.toUpperCase());
        System.out.println("É número? " + str.matches("\\d+"));
        System.out.println("É letra? " + str.matches("[a-zA-Z]+"));
        System.out.println("É alfanumérico? " + str.matches("[a-zA-Z0-9]+"));
        System.out.println("É decimal? " + str.matches("\\d+(\\.\\d+)?"));
        System.out.println("Está em maiúsculas? " + str.equals(str.toUpperCase()));
        System.out.println("Está em minúsculas? " + str.equals(str.toLowerCase()));
        System.out.println("Contém apenas espaços em branco? " + str.trim().isEmpty());

        scanner.close();
    }
}
