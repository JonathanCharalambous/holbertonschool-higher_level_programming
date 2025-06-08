#!/usr/bin/python3
import pickle

class CustomObject:
    
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try: 
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (EOFError, FileNotFoundError):
            print("File not found or empty.")
            return None
        
    def display(self):
        print("Name: {}, Age: {}, Is Student: {}".
              format(self.name, self.age, self.is_student))
