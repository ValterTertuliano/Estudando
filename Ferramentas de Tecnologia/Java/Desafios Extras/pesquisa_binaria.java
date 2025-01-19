public class Main {
	public static void main(String[] args) {
		int[] lista = {1, 2, 3, 4, 5};
		int alvo = 6;
		int posicao = pesquisa(lista, alvo);
		
		
		System.out.println("Pesquisa binaria: ");
		System.out.printf("Posição do alvo: %d", posicao);
		
	}
	public static int pesquisa(int[] lista, int alvo){
	int inicio = 0;
	int fim = lista.length - 1;
	
	while (inicio <= fim) {
	    int metade = (inicio + fim) / 2;
	    
	    if (lista[metade] == alvo){
	        return metade;
	    } else if (lista[metade] < alvo) {
	        inicio = metade + 1;
	    } else {
	        fim = metade - 1;
	    }
	}
	return -1;
}
}