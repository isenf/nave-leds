// ============================================================
// Project:     Nave Leds - Escape Room UTFPR-CP
// Author:      D. Fabro
// Date:        Jul 2026
// ============================================================

#include "config.h"
#include <FastLED.h>

// this is not my choice
LEDStrip<pin_leds[0], TOTAL_LEDS> stripA(name_leds[0]);
LEDStrip<pin_leds[1], TOTAL_LEDS> stripB(name_leds[1]);
LEDStrip<pin_leds[2], TOTAL_LEDS> stripC(name_leds[2]);
LEDStrip<pin_leds[3], TOTAL_LEDS> stripD(name_leds[3]);
LEDStrip<pin_leds[4], TOTAL_LEDS> stripE(name_leds[4]);
LEDStrip<pin_leds[5], TOTAL_LEDS> stripF(name_leds[5]);

StripBase *strips[] = {&stripA, &stripB, &stripC, &stripD, &stripE, &stripF};


void setup(){
    for(int i = 0; i< NUM_STRIPS; i++){
        strips[i]->begin();
        strips[i]->setBrightness(150);
        strips[i]->fill(CRGB::Red);
    }

    FastLED.show();

}

void loop(){

}

