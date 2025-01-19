public class Main {
    public static void main(String[] args) {
        System.out.print("Numero de Fibonnaci: 5\n");
        int fibo = fibonnaci(5);
        System.out.println("Resultado final da sequência: " + fibo);
    }

    public static int fibonnaci(int x) {
        int primeiro = 0;
        int segundo = 1;
        int fibo = 0;
        
        // Exibir os dois primeiros números da sequência
        System.out.println("0");
        System.out.println("1");
        System.out.println("----------------------------------------------");
        
        for (int i = 2; i <= x; i++) {
            fibo = primeiro + segundo;
            primeiro = segundo;
            segundo = fibo;
            System.out.printf("%d\n", fibo);
        }

        return fibo;
    }
}
