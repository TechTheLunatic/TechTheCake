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
}

/**
 * Placer ici les interruptions, minimiser le code (appels aux méthodes du singleton actionneurs)
 * 
 */
