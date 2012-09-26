#include "balise.h"

Balise::Balise() :
window_opener(-1),
distance(0),
last_distance_date(0) {

    // -----------------------
    // Timer
    // -----------------------

    timeout_timer::init();
    window_timer::init();

    // -----------------------
    // Liaison série
    // -----------------------

    serial_radio::init();
    serial_radio::change_baudrate(9600);

    // -----------------------
    // Diodes
    // -----------------------

    sbi(DDRD, DDD2);
    sbi(PORTD, PORTD2);

    // -----------------------
    // Interruptions
    // -----------------------

    sei();

    // Pins en input pour les PCINT
    cbi(DDRC, DDC0);
    cbi(DDRC, DDC1);
    cbi(DDRC, DDC2);
    cbi(DDRC, DDC3);

    // Pull up enabled
    sbi(PORTC, PORTC0);
    sbi(PORTC, PORTC1);
    sbi(PORTC, PORTC2);
    sbi(PORTC, PORTC3);

    // Active les interruptions PCINT
    sbi(PCMSK1, PCINT8);
    sbi(PCMSK1, PCINT9);
    sbi(PCMSK1, PCINT10);
    sbi(PCMSK1, PCINT11);
    sbi(PCICR, PCIE1);
}

void Balise::execute(char *order) {
    // Ping
    if (strcmp(order,"p") == 0) {
        serial_radio::print("ping");
    }
    // Demande de valeur de la dernière distance mesurée
    else if (strcmp(order,"v") == 0) {
        serial_radio::print(distance);
        serial_radio::print(last_distance_date);
    }
}

void Balise::diode_on() {
    sbi(PORTD, PORTD7);
}

void Balise::diode_blink() {
    diode_blink(50, 8);
}

void Balise::diode_blink(uint16_t period, uint8_t number) {
    for (uint8_t i = 1; i <= number; i++) {
        diode_on();
        for (uint16_t i = 1; i <= period; i++) _delay_ms(1);
        diode_off();
        for (uint16_t i = 1; i <= period; i++) _delay_ms(1);
    }
}

void Balise::diode_off() {
    cbi(PORTD, PORTD7);
}
