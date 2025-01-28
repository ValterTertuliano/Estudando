public class aula_6 {

    public static void main(String[] args) {
        
        // Maneira mais simples de declarar variáveis
        int idade = 3;
        float sal = 1830.54f;
        char letra = 'g'; // aceita apenas uma letra
        boolean casado = false;
        
        // Typecast 
        int idade2 = (int) 3;
        float sal2 = (float) 1820.65;
        char letra2 = (char) 'e';
        boolean casado2 = (boolean) false;

        // Chamando o objeto int - sendo Integer uma classe - wrapper class
        Integer idade3 = new Integer(3); // 4 bytes - aceita até 2_147_483_647
        Float sal3 = new Float(1820.54);
        Character letra3 = new Character('h'); // 1 byte / 8 bits
        Boolean casado3 = new Boolean(false); // 1 bit 

        // Corrigindo o formato da saída
        System.out.printf("Sua idade é %d", idade);
    }
}
