#ifndef CAPTEURS_H
#define CAPTEURS_H

#include <libintech/capteur_infrarouge.hpp>
#include <libintech/capteur_srf05.hpp>

#define NB_SRF_AVANT            1
#define NB_SRF_ARRIERE          1
#define NB_INFRAROUGE_AVANT     1
#define NB_INFRAROUGE_ARRIERE   1

/**
 * Gestion des actionneurs
 * 
 */
class Capteurs
{
	public:
        typedef Timer<1, 64> timer_capteur_us;
        typedef Timer<2, 1024> timer_refresh;
        
        typedef CapteurSRF< timer_capteur_us, AVR_PORTB<PORTB1>, AVR_PORTB<PORTB2> > capteur_us1_type;
        capteur_us1_type us1;
        typedef CapteurSRF< timer_capteur_us, AVR_PORTB<PORTB3>, AVR_PORTB<PORTB4> > capteur_us2_type;
        capteur_us2_type us2;

        typedef CapteurInfrarouge< AVR_ADC<PORTC0> > capteur_infra1_type;
        capteur_infra1_type inf1;
        typedef CapteurInfrarouge< AVR_ADC<PORTC1> > capteur_infra2_type;
        capteur_infra2_type inf2;    

	public:
		Capteurs();

};

#endif