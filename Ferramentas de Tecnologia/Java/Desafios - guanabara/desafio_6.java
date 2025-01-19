/*

Crie um script que peça um numero 
e exiba o dobro, triplo e a raiz quadrada
desse numero

*/

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Digite um numero: ");
		int num = scanner.nextInt();
		
		int dobro = num * 2;
		System.out.printf("\nDobro: %d", dobro);
		
		int triplo = num * 3;
		System.out.printf("\nTriplo: %d", triplo);
		
		double teste = Math.pow(num, 0.5);
		System.out.printf("\nRaiz Quadrada: %.2f", teste);
		
		scanner.close();
		
	
	}
}