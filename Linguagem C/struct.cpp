#include <stdio.h>

int main (void){
	struct horario
	{
		int horas;
		int minutos;
		int segundos;
		
	}; 
	
	struct horario agora;
	agora.horas = 3;
	agora.minutos = 42;
	agora.segundos = 12;
	
	printf("%i : %i: %i \n", agora.horas, agora.minutos, agora.segundos);
}
