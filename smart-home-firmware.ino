const int TEMP_SENSOR_PIN = A0; 
const int COOLING_FAN_PIN = 8;  

void setup() {
    pinMode(COOLING_FAN_PIN, OUTPUT);
}

void loop() {
    int rawTemp = analogRead(TEMP_SENSOR_PIN);
    if (rawTemp > 500) {
        digitalWrite(COOLING_FAN_PIN, HIGH);
    } else {
        digitalWrite(COOLING_FAN_PIN, LOW);
    }
}

