#ifndef DEF_AX12_HPP
#define DEF_AX12_HPP

// Librairie Standard
#include <avr/interrupt.h>
#include <avr/io.h>
#include <util/delay.h>

#include <libintech/utils.h>

#define AX_BROADCAST            0xFE        // Utilise le code 0xFE pour envoyer à tous les AX12

/** EEPROM AREA **/
#define AX_MODEL_NUMBER_L           0
#define AX_MODEL_NUMBER_H           1
#define AX_VERSION                  2
#define AX_ID                       3
#define AX_BAUD_RATE                4
#define AX_RETURN_DELAY_TIME        5
#define AX_CW_ANGLE_LIMIT_L         6
#define AX_CW_ANGLE_LIMIT_H         7
#define AX_CCW_ANGLE_LIMIT_L        8
#define AX_CCW_ANGLE_LIMIT_H        9
#define AX_SYSTEM_DATA2             10
#define AX_LIMIT_TEMPERATURE        11
#define AX_DOWN_LIMIT_VOLTAGE       12
#define AX_UP_LIMIT_VOLTAGE         13
#define AX_MAX_TORQUE_L             14
#define AX_MAX_TORQUE_H             15
#define AX_RETURN_LEVEL             16
#define AX_ALARM_LED                17
#define AX_ALARM_SHUTDOWN           18
#define AX_OPERATING_MODE           19
#define AX_DOWN_CALIBRATION_L       20
#define AX_DOWN_CALIBRATION_H       21
#define AX_UP_CALIBRATION_L         22
#define AX_UP_CALIBRATION_H         23

/** RAM AREA **/
#define AX_TORQUE_ENABLE            24
#define AX_LED                      25
#define AX_CW_COMPLIANCE_MARGIN     26
#define AX_CCW_COMPLIANCE_MARGIN    27
#define AX_CW_COMPLIANCE_SLOPE      28
#define AX_CCW_COMPLIANCE_SLOPE     29
#define AX_GOAL_POSITION_L          30
#define AX_GOAL_POSITION_H          31
#define AX_GOAL_SPEED_L             32
#define AX_GOAL_SPEED_H             33
#define AX_TORQUE_LIMIT_L           34
#define AX_TORQUE_LIMIT_H           35
#define AX_PRESENT_POSITION_L       36
#define AX_PRESENT_POSITION_H       37
#define AX_PRESENT_SPEED_L          38
#define AX_PRESENT_SPEED_H          39
#define AX_PRESENT_LOAD_L           40
#define AX_PRESENT_LOAD_H           41
#define AX_PRESENT_VOLTAGE          42
#define AX_PRESENT_TEMPERATURE      43
#define AX_REGISTERED_INSTRUCTION   44
#define AX_PAUSE_TIME               45
#define AX_MOVING                   46
#define AX_LOCK                     47
#define AX_PUNCH_L                  48
#define AX_PUNCH_H                  49

/** Instruction Set **/
#define AX_PING                     1
#define AX_READ_DATA                2
#define AX_WRITE_DATA               3
#define AX_REG_WRITE                4
#define AX_ACTION                   5
#define AX_RESET                    6
#define AX_SYNC_WRITE               131


template<class Serial_AX12>
class AX
{
	private:
		uint8_t id_;
		uint16_t angleMin_;
		uint16_t angleMax_;

		enum {
			READ_TIMEOUT = 0, READ_SUCCESS = 1
		};

		// Méthode pour envoyer un packet lisible par l'AX12
		void sendPacket(uint8_t datalength, uint8_t instruction, uint8_t *data)
		{
			uint8_t checksum = 0;
			Serial_AX12::send_char(0xFF);
			Serial_AX12::send_char(0xFF);
			Serial_AX12::send_char(id_);
			Serial_AX12::send_char(datalength + 2);
			Serial_AX12::send_char(instruction);

			checksum += id_ + datalength + 2 + instruction;

			for (uint8_t f=0; f<datalength; f++) {
				checksum += data[f];
				Serial_AX12::send_char(data[f]);
			}

			Serial_AX12::send_char(~checksum);
		}

		void static sendPacketB(uint8_t datalength, uint8_t instruction, uint8_t *data)
		{
			uint8_t checksum = 0;
			Serial_AX12::send_char(0xFF);
			Serial_AX12::send_char(0xFF);
			Serial_AX12::send_char(0xFE);
			Serial_AX12::send_char(datalength + 2);
			Serial_AX12::send_char(instruction);

			checksum += 0xFE + datalength + 2 + instruction;

			for (uint8_t f=0; f<datalength; f++) {
				checksum += data[f];
				Serial_AX12::send_char(data[f]);
			}

			Serial_AX12::send_char(~checksum);
		}

		/// Ecriture d'une séquence de bits 
		void writeData(uint8_t regstart, uint8_t reglength, uint16_t value) {
			uint8_t data [reglength+1];
			data[0] = regstart;
			data[1] = value&0xFF;
			if (reglength > 1) {data[2] = (value&0xFF00)>>8;}
			sendPacket(reglength+1, AX_WRITE_DATA, data);
		}

		void static writeDataB(uint8_t regstart, uint8_t reglength, uint16_t value) {
			uint8_t data [reglength+1];
			data[0] = regstart;
			data[1] = value&0xFF;
			if (reglength > 1) {data[2] = (value&0xFF00)>>8;}
			sendPacketB(reglength+1, AX_WRITE_DATA, data);
		}

		void readData(uint8_t regstart, uint8_t reglength, unsigned char *answer){
			uint8_t data[2];
			data[0] = regstart;
			data[1] = reglength;
			sendPacket(2, AX_READ_DATA, data);

			Serial_AX12::disable_tx();                   //désactiver la série sortante
			Serial_AX12::enable_rx();                   //activer la série entrante
			answer[0] = 0;
			while (answer[0] != 255) 
			{
				Serial_AX12::read_char(answer[0], 100); //attente du séparateur de trame 0xFF
			}
			while (answer[0] == 255) 
			{
				Serial_AX12::read_char(answer[0], 100); //évacuation du séparateur et de l'id
			}
			Serial_AX12::read_char(answer[0], 100);     //taille des données restantes à lire (nbDonnéesDemandées + 2 : avec toss_error et checksum)
			uint8_t length = answer[0] - 2;             //taille des données utiles            
			Serial_AX12::read_char(answer[0], 100);     //évacuation du toss_error
			for (uint8_t f=0; f<length; f++) {
				Serial_AX12::read_char(answer[f], 100); //lecture des données
			}    
			Serial_AX12::read_char(answer[0], 100);     //évacuation du checksum
			Serial_AX12::disable_rx();                  //désactiver la série entrante
			Serial_AX12::enable_tx();                   //réactiver la série sortante
		}


	public:

		AX(uint8_t id, uint16_t AX_angle_CW, uint16_t AX_angle_CCW)  // Constructeur de la classe
		{
			Serial_AX12::disable_rx();
			id_ = id;
			angleMin_=AX_angle_CW;
			angleMax_=AX_angle_CCW;
			init(AX_angle_CW, AX_angle_CCW);
		}

		AX(uint8_t id)  // Constructeur de la classe pour faire tourner l'AX12 en continu
		{
			Serial_AX12::disable_rx();
			id_ = id;
			angleMin_=0;
			angleMax_=0;
			init();
		}

		void init(uint16_t AX_angle_CW=0, uint16_t AX_angle_CCW=0)
		{
			// Active l'asservissement du servo
			writeData (AX_TORQUE_ENABLE, 1, 1);
			// Pas de limitation d'angles

			writeData (AX_CW_ANGLE_LIMIT_L, 2, AX_angle_CW);
			writeData (AX_CCW_ANGLE_LIMIT_L, 2, AX_angle_CCW);
			//baudrate
			writeData (AX_BAUD_RATE, 1, 0xCF);
		}
		/// Reset de l'AX12
		void reset() {
			sendPacketB(0x00, AX_RESET,0 );  
		}

		/* 
		 * Tente de réanimer un AX12 mort.
		 * L'argument baud_rate à passer en argument est le baud rate normal
		 * de fonctionnement de la série (9600)
		 */
		void reanimationMode(uint16_t baud_rate)
		{
			uint8_t debug_baudrate = 1;
			// On brute-force le baud rate des AX12, et on leur envoie pour chaque baud rate
			// d'écoute un signal de reset.
			while (debug_baudrate <= 0xFE)
			{
				Serial_AX12::change_baudrate(2000000/(debug_baudrate + 1));
				reset();
				debug_baudrate++;
			}

			// Une fois que le signal de reset a été reçu, l'AX12 écoute à 1.000.000 bps.
			// Donc à ce baud rate, on reflash le baud rate d'écoute de l'AX12.
			Serial_AX12::change_baudrate(1000000);

			for (int i=0; i<= 10; i++)
//				writeDataB(AX_BAUD_RATE, 1, uint8_t(2000000/baud_rate - 1));
				writeDataB(AX_BAUD_RATE, 1, 0xCF);

			Serial_AX12::change_baudrate(baud_rate);


			// Si l'id est différente du broadcast, alors on la reflash.
			uint8_t id_backup = id_;
			id_ = 0;
			initID(id_backup);
			id_ = id_backup;

			//init();
			// Puis on le fait osciller lentement en boucle infinie
			int i = 0;
			while ( i <= 2)
			{
				goTo(90);
				_delay_ms(900);
				goTo(100);
				_delay_ms(900);
				++i;
			}
		}


		/// Réinitialisation de l'ID de l'AX12
		void initID(uint8_t nouvel_id)
		{
			writeData(AX_ID, 1, nouvel_id);
		}

		void static initIDB(uint8_t nouvel_id)
		{
			writeDataB(AX_ID, 1, nouvel_id);
		}

		/// Goto - Envoyer un angle en DEGRES entre angleMin et angleMax
		void goTo(uint16_t angle)
		{
			writeData(AX_GOAL_POSITION_L, 2, (uint16_t)(((uint32_t)1023*angle)/300));
		}

		void static goToB(uint16_t angle)
		{
			writeDataB(AX_GOAL_POSITION_L, 2, (uint16_t)(((uint32_t)1023*angle)/300));
		}


		/// Changement de l'angle min
		void changeAngleMIN(uint16_t angleCW)
		{
			writeData(AX_CW_ANGLE_LIMIT_L, 2, angleCW);
		}

		void static changeAngleMINB(uint16_t angleCW)
		{
			writeDataB(AX_CW_ANGLE_LIMIT_L, 2, angleCW);
		}


		/// Changement de l'angle max
		void changeAngleMAX(uint16_t angleCCW)
		{
			writeData(AX_CCW_ANGLE_LIMIT_L, 2, angleCCW);
		}

		void static changeAngleMAXB(uint16_t angleCCW)
		{
			writeDataB(AX_CCW_ANGLE_LIMIT_L, 2, angleCCW);
		}


		/// Changement de la vitesse de rotation
		void changeSpeed(uint16_t vitesse)
		{
			writeData(AX_GOAL_SPEED_L, 2, 1023.*vitesse/100.);
		}

		void static changeSpeedB(uint16_t vitesse)
		{
			writeDataB(AX_GOAL_SPEED_L, 2, vitesse);
		}

		/// Désasservissement d'un AX12 branché.
		void unasserv()
		{
			writeData(AX_TORQUE_ENABLE, 1, 0);
		}

		void static unasservB()
		{
			writeDataB(AX_TORQUE_ENABLE, 1, 0);
		}

		// Changement de la limite de température
		void changeT(uint8_t temperature)
		{
			writeData(AX_LIMIT_TEMPERATURE, 1, temperature);
		}

		void static changeTB(uint8_t temperature)
		{
			writeDataB(AX_LIMIT_TEMPERATURE, 1, temperature);
		}

		// Changement du voltage maximal
		void changeVMax(uint8_t volt)
		{
			writeData(AX_UP_LIMIT_VOLTAGE, 1, volt);
		}

		void static changeVMaxB(uint8_t volt)
		{
			writeDataB(AX_UP_LIMIT_VOLTAGE, 1, volt);
		}


		// Changement du voltage minimal
		void changeVMin(uint8_t volt)
		{
			writeData(AX_DOWN_LIMIT_VOLTAGE, 1, volt);
		}

		void static changeVMinB(uint8_t volt)
		{
			writeDataB(AX_DOWN_LIMIT_VOLTAGE, 1, volt);
		}


		// LEDs d'alarme
		void led(uint8_t type)
		{
			writeData(AX_ALARM_LED, 1, type);
		}

		void static ledB(uint8_t type)
		{
			writeDataB(AX_ALARM_LED, 1, type);
		}

		// Lecture de la position courante, avec la notation de l'AX-12
		uint16_t getPosition_0_1023()
		{
			uint8_t pos[2];
			readData(AX_PRESENT_POSITION_L, 2, pos);    // 2 octet lus : le bit de poids fort aussi
			return (uint16_t)(((uint16_t)pos[1]<<8) | (uint8_t)(~pos[0]));
		}

		// Lecture de la position courante, en degrés
		uint16_t getPositionDegres()
		{
			return ((uint32_t)300*getPosition_0_1023())/1023;
		}

		// Retourne si l'AX-12 est en déplacement vers sa consigne
		bool isMoving()
		{
			uint8_t mov;
			readData(AX_MOVING, 1, mov);
			if (mov==0)
				return false;
			else
				return true;
		}

		// Pour envoyer un message comme un grand !
		void message(uint8_t adresse, uint8_t n, uint16_t val)
		{
			writeData(adresse, n, val);
		}

		void static messageB(uint8_t adresse, uint8_t n, uint16_t val)
		{
			writeDataB(adresse, n, val);
		}

		void lire(uint8_t regstart, uint8_t reglength, unsigned char *answer)
		{
			readData(regstart, reglength, answer);
		}
};

#endif
