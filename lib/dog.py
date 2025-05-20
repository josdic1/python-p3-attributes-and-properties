#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="empty", breed="Pug"):
        self.name = name
        self.breed = breed
    
    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed
    
    @name.setter
    def name(self, value):
        if type(value) is str and len(value) >= 1 and len(value) <= 25:
            self._name=value
        else:
            print("Name must be string between 1 and 25 characters.")

    @breed.setter
    def breed(self, value):
        if type(value) is str and value in APPROVED_BREEDS:
            self._breed=value
        else:
            print("Breed must be in list of approved breeds.")


