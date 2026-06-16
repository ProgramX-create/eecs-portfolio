#include <iostream>
unsigned char DDRB_REGISTER = 0b00000000; 
unsigned char PORTB_REGISTER = 0b00000000;

int main() {
    DDRB_REGISTER |= (1 << 5); 
    PORTB_REGISTER |= (1 << 5);
    std::cout << "Port Data Register Output: Pin 5 Driven High\n";
    return 0;
}

