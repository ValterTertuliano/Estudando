import java.util.Scanner;

public class desafio_2 {
    public static void main(String[] args) {
        
    int ano, mes, dia;
    
    Scanner scanner = new Scanner(System.in);
    
    System.out.println("Digite o Ano de nascimento: ");
    ano = scanner.nextInt();

    System.out.println("Digite o mes de nascimento: ");
    mes = scanner.nextInt();

    System.out.println("Digite o Dia do nascimento: ");
    dia = scanner.nextInt();

    System.out.println("A pessoa nasceu no dia " + dia + "/"+ mes + "/" +  ano);

    scanner.close();

    }   
}
