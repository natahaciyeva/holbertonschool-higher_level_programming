#!/usr/bin/env python3
from abc import ABC, abstractmethod

# Abstrakt sinif
class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Return the sound of the animal"""
        pass

# Dog sinifi abstrakt Animal sinifindən miras alır
class Dog(Animal):
    def sound(self):
        return "Bark"

# Cat sinifi abstrakt Animal sinifindən miras alır
class Cat(Animal):
    def sound(self):
        return "Meow"
