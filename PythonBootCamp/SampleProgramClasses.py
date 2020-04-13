# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:01:24 2020

@author: srira
"""


class Patient(object):
    ''' '''
    status = 'Patient'
    def __init__(self, name, age):
            self.name = name
            self.age = age
            self.conditions = []
    
    def get_details(self):
        print(f'Patient name {self.name} and {self.age} years and patient is {self.conditions}')
        
    def add_details(self, patientcondition):
        self.conditions.append(patientcondition)
            
            
Steve = Patient('Steve Smith',34)
Kohli = Patient('Virat Kohli',34)
Kohli.add_details('Health is good')
            

