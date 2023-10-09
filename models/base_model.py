#!/usr/bin/python3
from datetime import datetime 
import uuid

class BaseModel:
    '''class that defines all the common attributes/methods for other classes'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def updated(self):
        self.created_at = datetime.now()

    def save(self):
        self.updated()

    def __str__(self):



if __name__ == '__main__':
    my_model = BaseModel
