// rq : cet actionneur a pour réponse 7 au ping

// LIBRAIRIES STANDARD
#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>

// LIBRAIRIE INTECH
#include <libintech/serial/serial_0_interrupt.hpp>
#include <libintech/serial/serial_0.hpp>
#include <libintech/serial/serial_1_interrupt.hpp>
#include <libintech/serial/serial_1.hpp>

// LIBRAIRIES LOCALES
#include <libintech/ax12.hpp>
#define BAUD_RATE_SERIE 9600
#define AX_ANGLECW              205 //angle min >0
#define AX_ANGLECCW             818 //angle max <1024

#define AQUITTER serial_PC_::print("_")

typedef Serial<0> serial_PC_;
typedef Serial<1> serial_AX_;

typedef AX<serial_AX_> AX12;

int main () {
  serial_PC_::init();
  serial_PC_::change_baudrate(BAUD_RATE_SERIE);
  serial_AX_::init();
  serial_AX_::change_baudrate(BAUD_RATE_SERIE);

  AX12 AX12_BRAS_BAS(3, AX_ANGLECW, AX_ANGLECCW);
  AX12 AX12_BRAS_HAUT(1, AX_ANGLECW, AX_ANGLECCW);
  
// 3 pour l'actionneur du bas
// 1  pour l'actionneur du haut
  while(1){
    
    char buffer[17];
    serial_PC_::read(buffer);
    AQUITTER;
    /// ************************************* ///
    /// début des cas de commande possibles   ///
    /// ************************************* ///

    //ping
    if (strcmp(buffer, "?") == 0)
    {
      serial_PC_::print(7);
    }

    /// *********************************************** ///
    ///                 ACTIONNEURS                     ///
    /// *********************************************** ///
    else if(strcmp(buffer, "bas") == 0)
    {
      uint8_t id;
      uint16_t angle;

      serial_PC_::read(angle);
      AQUITTER;
      AX12_BRAS_BAS.goTo(angle); //Angle d'entrée commandé
    }
    
    else if(strcmp(buffer, "haut") == 0)
    {
      uint8_t id;
      uint16_t angle;

      serial_PC_::read(angle);
      AQUITTER;
      AX12_BRAS_HAUT.goTo(angle); //Angle d'entrée commandé
    }
    
    
    //fin des commandes possibles
  }
  return 0;
}
