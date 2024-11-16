import json
import os

class SingletonJson:
    """
    singleton class handle json based persistance
    """
    
    _instance ={}
    
    def __new__(cls, db_path, *args, **kwargs):
        if db_path not in cls._instance:
            cls._instance[db_path] = super(SingletonJson, cls).__new__(cls)
            cls._instance[db_path]._db_path = db_path
            cls._instance[db_path]._data = None
            cls._instance[db_path]._load()
        
        return cls._instance[db_path]
    
    def _load(self):
        if not os.path.exists(self._db_path):
            with open(self._db_path, 'w') as f:
                json.dump({}, f)
        with open(self._db_path, "r") as f:
            self._data = json.load(f)
    
    def save(self):
        with open(self._db_path, "w") as f:
            json.dump(self._data, f, indent=4)
            
    def get_data(self):
        return self._data
    
    def update_data(self, data):
        self._data = data
        self.save() 
