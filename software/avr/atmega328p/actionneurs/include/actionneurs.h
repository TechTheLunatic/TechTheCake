#ifndef ACTIONNEURS_H
#define ACTIONNEURS_H

#include <libintech/singleton.hpp>
#include <libintech/serial/serial_0.hpp>
#include <libintech/pwm.hpp>
#include <libintech/moteur.hpp>

#include "ascenceur.h"

/**
 * Gestion des actionneurs
 * 
 */
class Actionneurs : public Singleton<Actionneurs>
{
	public:
		typedef Serial<0> serie;
		typedef Moteur< PWM<0,ModeFastPwm,1,'A'>, AVR_PORTB <PORTB5> >  moteur_avant_t;
		/**
		 * Ascenceur avant, dépend d'un moteur
		 * 
		 */
		Ascenceur< moteur_avant_t > ascenceur_avant;

	public:
		Actionneurs();
		
		/**
		 * Execute les ordres reçus sur la série
		 * 
		 */
		void execute(char*);

};

#endif
