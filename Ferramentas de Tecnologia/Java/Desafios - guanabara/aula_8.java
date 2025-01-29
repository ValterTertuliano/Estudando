import java.util.Scanner;

public class aula_8 {
    public static void main(String[] args) {
     
        int n1, n2, n3, resultado;
        n1 = 14;
        n2 = 10;
        n3 = 12;
        resultado = (n1 < n2)?0:1;
         
        boolean r = (n1 > n2 && n1 > n3)?true:false;
        
        System.out.println("Resultado: " + resultado);
        System.out.println("Resultado de 'E'(&&): " + r);

        //---------------------------------------------------
        int idade;
        System.out.print("Digite sua idade: ");
        Scanner scanner= new Scanner(System.in);
        idade = scanner.nextInt();

        String vota = ((idade >= 16 && idade<18) || (idade > 70))?"é opcional":"Não é opcional"; 
         System.out.println("Seu Voto: " + vota);


    }
}
