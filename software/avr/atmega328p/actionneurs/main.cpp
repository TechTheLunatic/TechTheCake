#include <libintech/serial/serial_0_interrupt.hpp>
#include <libintech/serial/serial_0.hpp>

#include "actionneurs.h"

int main() 
{
	Actionneurs &actionneurs = Actionneurs::Instance();
    
    while(1)
    {
		char buffer[20];
        Actionneurs::serie::read(buffer);
        actionneurs.execute(buffer);
    }
	return 0;
}

/**
 * Placer ici les interruptions, minimiser le code (appels aux méthodes du singleton actionneurs)
 * 
 */
ISR(TIMER1_OVF_vect)
{
	Actionneurs &actionneurs = Actionneurs::Instance();
	actionneurs.ascenceur_avant.codeuse(roue1);
	actionneurs.ascenceur_avant.asservir();
}

ISR(TIMER0_OVF_vect)
{
}

ISR(TIMER2_OVF_vect)
{
}