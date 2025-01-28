public class aula_7 {
    public static void main(String[] args) {
        int n1 = 5;
        int n2 = 15;

        // Operações matemáticas
        int adicao = n1 + n2;
        int multiplicacao = n1 * n2;
        float divisao = (float) n1 / n2; // Typecast para float
        int subtracao = n1 - n2;

        // Incremento e Decremento
        adicao++;
        divisao -= 1; // Ajustado o decremento

        // Saída formatada
        System.out.printf("Adição: %d%n", adicao);
        System.out.printf("Multiplicação: %d%n", multiplicacao);
        System.out.printf("Divisão: %.2f%n", divisao); // Formatação para float com 2 casas decimais
        System.out.printf("Subtração: %d%n", subtracao);
    }
}
