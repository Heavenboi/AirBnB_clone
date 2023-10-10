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
        self.update_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def to_dict(self):
        ''' returns a dictionary containing all keys/value of __dict__ of instance '''
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__

        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict
