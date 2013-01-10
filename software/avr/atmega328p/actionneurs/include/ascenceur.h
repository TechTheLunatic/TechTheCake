#ifndef ASCENCEUR_H
#define ASCENCEUR_H

#include <libintech/moteur.hpp>
#include <libintech/asservissement.hpp>

#define COMPTEUR_BLOCAGE_MAX 30 // ~ 1 sec (à vérifier)

enum AscenseurPosition {ASCENSEUR_HAUT = 46000, ASCENSEUR_BAS = 0};

template<class Moteur>
class Ascenceur
{
	public:
		
		Ascenceur();
		void asservir();
		void consigne(int32_t consigne);
		void consigne(AscenseurPosition);
		void codeuse(int32_t);
		int32_t codeuse();
		void desasservir();
		void reasservir();
						
	private:
	
		Moteur _moteur;
		Asservissement _asservissement;		
		int32_t _codeuse;
		uint8_t _compteur_blocage;
		bool _asservir;
	
	public:

		bool _bloc_en_bas;
		
};

#endif
