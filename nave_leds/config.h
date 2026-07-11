// ============================================================
// Project:     Nave Leds - Escape Room UTFPR-CP
// Author:      D. Fabro
// Date:        Jul 2026
// ============================================================

#include <FastLED.h>
// const variables
#define LEDS_LAT 18
#define LEDS_DIAG 19
const uint8_t TOTAL_LEDS =  LEDS_LAT + LEDS_DIAG;
#define LED_TYPE WS2812B
#define COLOR_ORDER GRB

// led strip config
const uint8_t pin_leds = {2, 3, 4, 5, 6, 7};

template<uint8_t PIN, uint8_t N>
struct LEDStrip{
    char name;
    CRGB* leds[N];
    CLEDController* controller;

    LEDStrip() : controller(nullptr){}

    void begin(){
        controller = &FastLED.addLeds<LED_TYPE, PIN, COLOR_ORDER>(leds, N);
    }

    void setBrightness(uint8_t brightness){
        if(controller) controller->setBrightness(brightness);
    }



}

