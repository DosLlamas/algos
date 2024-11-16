#include <stdio.h>

// Same typedef syntax as struct
typedef enum TrafficLightState TrafficLightState;
typedef enum Day Day;

// Days of the week
enum Day{Sun, Mon, Tue, Wed, Thu, Fri, Sat}; 

// Simulating the traffic light control system
enum TrafficLightState {
    RED = 'R',
    YELLOW = 'Y',
    GREEN = 'G'
};

// Function to determine the action based on the current state
void handleTrafficLight(enum TrafficLightState state) {
    switch (state) {
        case RED:
            printf("%s%c%s", "Stop! The light is ", RED, ".\n");
            break;
        case YELLOW:
            printf("%s", "Caution! The light is yellow.\n");
            break;
        case GREEN:
            printf("%s", "Go! The light is green.\n");
            break;
        default:
            printf("%s", "Invalid traffic light state!\n");
    }
}

int main(){
    Day sunday = Sun;
    printf("Day: %d\n", sunday);

    TrafficLightState currentState = RED;
    
    // Print the current action based on traffic light state
    handleTrafficLight(currentState);
    
    // Change to yellow light
    currentState = YELLOW;
    handleTrafficLight(currentState);
    
    // Change to green light
    currentState = GREEN;
    handleTrafficLight(currentState);

    const int BLUE = 3;
    currentState = BLUE;
    handleTrafficLight(currentState);

    return 0;
}
