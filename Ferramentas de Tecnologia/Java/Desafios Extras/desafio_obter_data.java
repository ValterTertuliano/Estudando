import java.util.Scanner; // Coletar entradas

public class Main {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        
        // Coletar dia
        System.out.print("Digite o dia de nascimento: ");
        int dia = scanner.nextInt();
        
        // Limpar buffer após scanner.nextInt()
        scanner.nextLine();
        
        // Coletar mês
        System.out.print("Digite o mês de nascimento (nome do mês): ");
        String mes = scanner.nextLine();
        
        // Coletar ano
        System.out.print("Digite o ano de nascimento: ");
        int ano = scanner.nextInt();
        
        // Exibir data formatada
        System.out.printf("Você nasceu no dia %d de %s de %d.\n", dia, mes, ano);
        
        // Fechar scanner
        scanner.close();
        
        return 0;
    }
}
