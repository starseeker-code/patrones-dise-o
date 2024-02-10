import abc

# |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
# | Single responsibility |
# |_______________________|

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
        
class File(Reader, Compressor, Connector):  # This way behaviour is spread between cohesionated classes and aggregated in a composed, final File class
    def __init__(self, path: str, size: int = 0):
        self.path = path
        self.size = size
        
    def info(self) -> dict:
        return {"path": self.path,
                "size": self.size}



# |‾‾‾‾‾‾‾‾‾‾‾‾‾|
# | Open/Closed |
# |_____________|

### Violation
    
class AdminUser:
    def access_database(self):
        print("I have unrestricted access to the database")
    
class NormalUser:
    def access_database(self):
        print("I have no permissions to write or read the database")
    
class UserService:
    def __init__(self, user_type: str = "normal"):
        self.user_type = user_type.lower()
        
    def check_privileges(self):  # In case a third user is to be added, this design forces changes in the UserService class, and shouldn't happen
        if self.user_type == "normal":
            print("I have no permissions to write or read the database")
        elif self.user_type == "admin":
            print("I have unrestricted access to the database")

### Correct design

class IUser(abc.ABC):
    @abc.abstractmethod
    def access_database(self):
        pass

class AdminUser(IUser):
    def access_database(self):
        print("I have unrestricted access to the database")
    
class NormalUser(IUser):
    def access_database(self):
        print("I have no permissions to write or read the database")
        
class CurrentUser:  # This class will be the connection between the user types and the UserService
    @property
    def user_type(self):
        return NormalUser()
        
    @user_type.setter
    def user_type(self, user_type: IUser = NormalUser()):
        self.user_type = user_type

class UserService:
    @staticmethod
    def check_privileges():
        CurrentUser().user_type.access_database()
        
# And now, adding a new user type is as simple as extending the IUser interface with a DataUser. No modification is needed
class DataUser(IUser):
    def access_database(self):
        print("I can only read the database, but not write")



# |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
# | Liskov substitution |
# |_____________________|

### Violation



### Correct design





# |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
# | TODO: Principio 4 - Interface segregation |
# |___________________________________________|

### Violation



### Correct design





# |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
# | TODO: Principio 5 - Dependency inversion (inyection) |
# |______________________________________________________|

### Violation



### Correct design




































































































def connect(arg):  # Ignore this function, used in example
    pass