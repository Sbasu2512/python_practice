from abc import ABC, abstractmethod


class Switch(ABC):
    @abstractmethod
    def switch_on(self):
        pass

    @abstractmethod
    def switch_off(self):
        pass


class PlasticSwitch(Switch):

    def switch_on(self):
        print("Plastic Switch is on")

    def switch_off(self):
        print('Plastic Switch is off')

    def emergency_indicator(self):
        print('Emergency Indicator Toggle')


class WifiSwitch(Switch):

    def switch_on(self):
        print("Wifi Switch is on")

    def switch_off(self):
        print('Wifi Switch is off')

