from abc import ABC, abstractmethod
from typing import List

# Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, state: str):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class TrafficLight(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = "RED"

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

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

# Builder Pattern
class Street:
    def __init__(self, name: str, crossings: int):
        self.name = name
        self.crossings = crossings

    def __str__(self):
        return f"Street: {self.name}, Crossings: {self.crossings}"

class StreetBuilder:
    def __init__(self):
        self.name = ""
        self.crossings = 0

    def set_name(self, name: str):
        self.name = name
        return self

    def set_crossings(self, crossings: int):
        self.crossings = crossings
        return self

    def build(self) -> Street:
        return Street(self.name, self.crossings)

if __name__ == "__main__":
    # Traffic light
    traffic_light = TrafficLight()

    # Cars
    car1 = Car(1)
    car2 = Car(2)
    car3 = Car(3)

    traffic_light.attach(car1)
    traffic_light.attach(car2)
    traffic_light.attach(car3)

    # Traffic light change
    traffic_light.change_state("GREEN")
    traffic_light.change_state("RED")

    # Sreet using builder
    street_builder = StreetBuilder()
    main_street = (
        street_builder
        .set_name("Moscova bd.")
        .set_crossings(3)
        .build()
    )

    print(main_street)

    side_street = (
        street_builder
        .set_name("Studentilor Street")
        .set_crossings(1)
        .build()
    )

    print(side_street)
