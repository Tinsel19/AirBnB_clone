#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    ''' defines the user class elements '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
