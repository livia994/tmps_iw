Individual Work: Traffic Simulation
----------------------------------------
### Author: Gîncu Olivia & Barbarov Nadejda

### Objectives:
- Get familiar and implement the Observer and Builder Pattern
- Create a simulation of traffic in a city

### Domain:
For this project, we had to implement the observer and builder pattern in a simulation of traffic on streets that have traffic lights and crossings.

### Used Design Patterns:
1. Observer: Creates a one-to-many relationship where `TrafficLight` notifies the `Car` observers of its state changes, telling them how to react.
2. Builder: Provides a step-by-step creation process for the `Street` objects. 
### Implementation:
For this project, we have used Python which follows object-oriented principles to implement Builder and Observer Pattern.

### 1. Observer Pattern:
- `TrafficLight` controls a list of `Car` observers and notifies them when its state changes using `notify()`.
- `Car` reacts to the state change in `update()` by printing its action (stopping or moving).

### Code snippet:
```
class TrafficLight(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = "RED"

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def change_state(self, state: str):
        print(f"Traffic light changes to {state}")
        self._state = state
        self.notify()

class Car(Observer):
    def __init__(self, car_id: int):
        self.car_id = car_id

    def update(self, state: str):
        if state == "GREEN":
            print(f"Car {self.car_id} is moving.")
        elif state == "RED":
            print(f"Car {self.car_id} is stopping.")

```
### Purpose:
The `TrafficLight` notifies `Car` objects when its state changes, allowing cars to react at the light.

### 2. Builder Pattern:
- `StreetBuilder` has methods (set_name, set_crossings) to set street attributes.
- The `build()` method returns the created `Street` object.

### Code Snippet:
```
class Street:
    def __init__(self, name: str, length: int, crossings: int):
        self.name = name
        self.length = length
        self.crossings = crossings

class StreetBuilder:
    def __init__(self):
        self.name = ""
        self.length = 0
        self.crossings = 0

    def set_name(self, name: str):
        self.name = name
        return self

    def set_length(self, length: int):
        self.length = length
        return self

    def set_crossings(self, crossings: int):
        self.crossings = crossings
        return self

    def build(self) -> Street:
        return Street(self.name, self.length, self.crossings)

```
### Purpose:
Constructs `Street` objects step-by-step with the attributes name and crossings.

### Conclusion:
This program simulates a city with traffic lights, cars, and streets using two desing patterns. The **Observer Pattern** helps traffic lights notify cars to stop or move when the light changes. The **Builder Pattern** makes it easy to create streets with details like name and crossings. This individual work was interisting and helped us have get some more experience in  design patterns.

