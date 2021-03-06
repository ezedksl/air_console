from datetime import datetime
import uuid
from . import storage


class BaseModel():
    """Base class for the console

    """
    def __init__(self, *args, **kwargs):
        """instance initiation method

        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the print() and str() representation

        """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """saves the instance and updated the updated_at time

        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return the dictionary of the instance

        """
        inst_dict = dict(self.__dict__)
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict
