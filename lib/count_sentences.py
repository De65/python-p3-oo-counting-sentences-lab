#!/usr/bin/env python3

class MyString:
    def __init__(self, v=""):
        self._value = v
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        try:
            if self._value.index("."):
                return True
            else:
                return False
        except:
            return False
        
    def is_question(self):
        try:
            if self._value.index("?"):
                return True
            else:
                return False
        except:
            return False
    
    def is_exclamation(self):
        try:
            if self._value.index("!"):
                return True
            else:
                return False
        except:
            return False
        
    def count_sentences(self):
        count = 0
        spl = self._value.split(" ")
        for el in spl:
            if el.__contains__('.') or el.__contains__('!') or el.__contains__('?'):
                count+=1
        return count 
    value = property(get_value,set_value)