#!/usr/bin/python3

"""
Base class for
all modules
"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    class from which others
    class inherits from, with
    public instances of id,
    created_at and updated_at
    """

    def __init__(self, *args, **kwargs):
        """
        instantiate public
        instances
        """

        if len(kwargs) == 0 or kwargs is None:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            return
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key is not "__class__":
                    self.__dict__[key] = value

    def __str__(self):
        """
        string representation of
        object
        """

        stg = "[{}] ({}) {}"
        return stg.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        modify public instance updated_at
        with the current date and time
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        return dictionary with key/value
        of the __dict__ of the instance
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
