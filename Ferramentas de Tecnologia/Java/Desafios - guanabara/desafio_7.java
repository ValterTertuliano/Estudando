/*

Programa que lê as duas notas de um 
aluno, calcula a média entre elas e exibe o
resultado.

*/

import java.util.Scanner;

public class desafio_7 {
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Nota 1: ");
		float nota1 = scanner.nextFloat();
		
		System.out.printf("Nota 2: ");
		float nota2 = scanner.nextFloat();
		
		float media = (nota1 + nota2) / 2;
		System.out.printf("Média: %.2f", media);
		
		scanner.close();
		
	}
}