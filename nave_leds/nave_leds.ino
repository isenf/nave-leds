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
        strips[i]->fill(CRGB::Black);
    }

    FastLED.show();

}

void loop(){
    arrowHor(CRGB::Cyan, true); // left
    arrowHor(CRGB::Red, false); // right
    arrowVer(CRGB::Cyan, true); // up
    arrowVer(CRGB::Pink, false);  // down  
}

void arrowHor(CRGB color, bool left){
    int idx1 = -1, idx2 = -1;

    if(left){
        idx1 = 2;
        idx2 = 3;
    } else{
        idx1 = 5;
        idx2 = 0;
    }

    for(int i = 0; i < LEDS_LAT; i++){
        strips[idx1]->setPixel(LEDS_DIAG+i, color);
        strips[idx2]->setPixel(1+i, color);
        strips[idx2]->setPixel(TOTAL_LEDS-i-1, color);

        FastLED.show(); // change this later
        strips[idx1]->setPixel(LEDS_DIAG+i, CRGB::Black);
        strips[idx2]->setPixel(1+i, CRGB::Black);
        strips[idx2]->setPixel(TOTAL_LEDS-i-1, CRGB::Black);
        delay(200);
    }   
}

void arrowVer(CRGB color, bool up){
    int idx1 = -1, idx2 = -1;

    if(up){
        idx1 = 1;
        idx2 = 2;
    } 
    else{
        idx1 = 4;
        idx2 = 5;
    }

    for(int i = 0; i < LEDS_LAT + LEDS_LAT/2 + 1; i ++){
        strips[idx1]->setPixel(i, color);

        if(i <= LEDS_LAT){
            strips[idx2]->setPixel(i, color);
        } else{
            strips[idx1]->setPixel(TOTAL_LEDS + LEDS_LAT - i, color);
        }

        FastLED.show();
        // change this later
        strips[idx1]->setPixel(i, CRGB::Black);
        if(i <= LEDS_LAT){
            strips[idx2]->setPixel(i, CRGB::Black);
        } else{
            strips[idx1]->setPixel(TOTAL_LEDS + LEDS_LAT - i, CRGB::Black);
        }

        delay(200);
    }
}




