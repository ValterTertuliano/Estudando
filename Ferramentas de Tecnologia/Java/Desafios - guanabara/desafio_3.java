import java.util.Scanner;

public class desafio_3 {
    public static void main(String[] args) {
        
        float num1, num2, somar;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um numero: ");
        num1 = scanner.nextFloat();

        System.out.println("Digite outro numero: ");
        num2 = scanner.nextFloat();

        somar = num1 + num2;
        System.out.println("Total: " + somar);

        scanner.close();
    }
}
