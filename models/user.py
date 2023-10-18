#!/usr/bin/python3
'''
this is user class
'''
#import models
from base_model import BaseModel

class User(BaseModel):
    '''
    user class that inherits from BaseModel
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
