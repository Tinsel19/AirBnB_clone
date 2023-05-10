#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    '''  defines the review class elements '''
    place_id = ''
    user_id = ''
    text = ''
