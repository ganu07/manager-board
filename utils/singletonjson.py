

import json
import os
import uuid
from datetime import datetime


class SingletonJson:
    """
    singleton class handle json based persistance
    """
    
    _instance ={}
    
    def __new__(cls, db_path, *args, **kwargs):
        pass