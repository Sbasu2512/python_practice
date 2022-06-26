from abc import ABC, abstractmethod

# Java, golang, C#, C++ -> interface is a keyword
# Python does not support the keyword interface
# Any class that Inherits ABC is an interface
class Card(ABC):

    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def get_subscription_fee(self):
        pass

    @abstractmethod
    def update_transaction_amount(self, amount):
        pass

    @abstractmethod
    def get_limit(self):
        pass
