#!/usr/bin/python3
""" This module is used for the Base Model of the AirBNB Clone """
from datetime import datetime
import uuid
import models


class BaseModel():
    """
    defines all common attributes/methods for other classes
    Public instance attributes
    id - string assigned with uuid when an instance is created
    created_at - current datetime when an instance is created
    updated_at - current datetime updated when object is changed
    __str__ - should print [<class name>] (<self.id>) <self.__dict__>
    Public instance methods
    save(self) - updates updated_at with current datetime
    to_dict(self) - returns a dictionary representation of the instance
    by using self.__dict__ only instance attributes are returned
    a key __class__ must be added to the dictionary w class name of object
    created_at and updated_at must be converted to string object in ISO format
    """
    def __init__(self, *args, **kwargs):
        """ initialization """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value

                elif key == "created_at" or key == "updated_at":
                    s_time = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, s_time)

                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """  updates the public instance attribute updated_at with the
        current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary of the instance """
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        if isinstance(self.created_at, datetime) is True:
            new_dict['created_at'] = datetime.isoformat(self.created_at)
        if isinstance(self.updated_at, datetime) is True:
            new_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return new_dict

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
