import abc


# Single responsibility

### Violation

class File:
    def __init__(self, path: str, size: int = 0):
        self.path = path
        self.size = size
        
    def info(self) -> dict:
        return {"path": self.path,
                "size": self.size}
    
    def read(self):
        print(f"Reading file {self.path}")
        
    def write(self, message: str):
        print(f"Writing file {self.path}")
        
    def compress(self):
        print(f"Compressing file {self.path}")
        
    def decompress(self):
        print(f"Decompressing file {self.path}")
        
    def connect_to_db(self, db_address: str):
        try:
            connect(db_address)
            print(f"Connected file {self.path} to {db_address}")
        except ConnectionError:
            ...

### Correct design

class Reader(abc.ABC):
    def read(self):
        print(f"Reading file {self.path}")
        
    def write(self, message: str):
        print(f"Writing file {self.path}")
        
class Compressor(abc.ABC):
    def compress(self):
        print(f"Compressing file {self.path}")
        
    def decompress(self):
        print(f"Decompressing file {self.path}")
        
class Connector(abc.ABC):
    def connect_to_db(self, db_address: str):
        try:
            connect(db_address)
            print(f"Connected file {self.path} to {db_address}")
        except ConnectionError:
            ...
        
class File(Reader, Compressor, Connector):
    def __init__(self, path: str, size: int = 0):
        self.path = path
        self.size = size
        
    def info(self) -> dict:
        return {"path": self.path,
                "size": self.size}



# TODO: Principio 2 - Open/Closed



# TODO: Principio 3 - Liskov substitution



# TODO: Principio 4 - Interface segregation



# TODO: Principio 5 - Dependency inversion (inyection)




































































































def connect(arg):  # Ignore this function, used in example
    pass