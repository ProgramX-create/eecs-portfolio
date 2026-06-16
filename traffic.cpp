#include <iostream>
enum TrafficState { RED, GREEN, YELLOW };

void run_state_machine(TrafficState current) {
    if(current == GREEN) std::cout << "System Active: GREEN.\n";
    if(current == YELLOW) std::cout << "Warning: YELLOW.\n";
    if(current == RED) std::cout << "Halt: RED.\n";
}

int main() {
    run_state_machine(GREEN);
    return 0;
}

