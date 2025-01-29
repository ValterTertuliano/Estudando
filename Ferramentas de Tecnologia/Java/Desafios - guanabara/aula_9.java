import java.util.Scanner;

public class aula_9 {
    public static void main(String[] args) {
        
        float n1, n2, total;
        
        System.out.print("Digite a primeira nota: ");
        Scanner scanner = new Scanner(System.in);
        n1 = scanner.nextFloat();

        System.out.print("Digite a segunda nota: ");
        n2 = scanner.nextFloat();

        total = (n1 + n2) / 2;
        if (total < 6){
        System.out.println("A média é " + total + " Você está reprovado");
    } else {
            System.out.println("A média é " + total + " Você está Aprovado");
            
        }

    }
}
