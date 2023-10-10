#!/usr/bin/python3
import models
from datetime import datetime 
import uuid

class BaseModel:
    '''class that defines all the common attributes/methods for other classes'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.update_at.now()

    def __str__(self):
        return "[{}] ({}){}".format(self.__class__.__name__, self.id, self.__dict__)



if __name__ == '__main__':
    my_model = BaseModel
