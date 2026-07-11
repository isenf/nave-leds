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
#define NUM_STRIPS 6

// config the strips
constexpr uint8_t pin_leds[] = {2, 3, 4, 5, 6, 7};
const char name_leds[] = {'A', 'B', 'C', 'D', 'E', 'F'};

// structs for led strip
struct StripBase{
    virtual void begin() = 0;
    virtual void setBrightness(uint8_t) = 0;
    virtual void fill(CRGB) = 0;
    virtual void show() = 0;
    virtual void clear() = 0;
    virtual ~StripBase() {}
};

template<uint8_t PIN, uint8_t N> // N -> number of leds in the strip
struct LEDStrip : public StripBase{
    char name;
    CRGB leds[N];
    CLEDController* controller;

    // constructor
    LEDStrip(char n) : name(n), controller(nullptr){}

    void begin(){
        controller = &FastLED.addLeds<LED_TYPE, PIN, COLOR_ORDER>(leds, N);
    }

    void setBrightness(uint8_t brightness) {
        FastLED.setBrightness(brightness);
    }

    void fill(CRGB color){
        fill_solid(leds, (int)N, color);
    }

    void setPixel(uint8_t index, CRGB color){
        if( index < N) leds[index] = color;
    }

    void show(){
        FastLED.show();
    }

    void clear(){
        fill(CRGB::Black);
    }

};




