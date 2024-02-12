import abc
from typing import Self

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





# |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
# | Interface segregation |
# |_______________________|

### Violation

class IFileHandler(abc.ABC):
    def authenticate(self):
        auth_user(self._id)

    @abc.abstractmethod
    def connect_to_db(self, db_address: int):
        pass

    @abc.abstractmethod
    def convert_audio(self, audio_format: str):
        pass

    @abc.abstractmethod
    def convert_video(self, video_format: str):
        pass

    @abc.abstractstaticmethod
    def play():
        pass

class DBConnection(IFileHandler):
    def __init__(self, id: int):
        self._id = id
        try:
            self.authenticate()
        except ValueError as error:
            print("There was an error with the user authentication")
            print(error)
    
    def connect_to_db(self, db_address: str):
        try:
            connect(db_address)
        except ValueError:
            print("The database address is not valid")

class AudioFile(IFileHandler):
    def __init__(self, format: str):
        self.format = format
    
    def convert_audio(self, audio_format: str):
        if audio_format in VALID_AUDIO_FORMATS:
            self.format = audio_format

    @staticmethod
    def play():
        print("Playing the audio file")

class VideoFile(IFileHandler):
    def __init__(self, format: str):
        self.format = format
    
    def convert_audio(self, video_format: str):
        if video_format in VALID_VIDEO_FORMATS:
            self.format = video_format

    @staticmethod
    def play():
        print("Playing the video file")

### Correct design

class IAuthenticate(abc.ABC):
    def authenticate(self):
        auth_user(self._id)

class IPlayable(abc.ABC):
    @abc.abstractstaticmethod
    def play():
        pass

class IAudioConverter(abc.ABC):
    @abc.abstractmethod
    def convert_audio(self, audio_format: str):
        pass

class IVideoConverter(abc.ABC):
    @abc.abstractmethod
    def convert_video(self, video_format: str):
        pass

class DBConnection(IAuthenticate):
    def __init__(self, id: int):
        self._id = id
        try:
            self.authenticate()
        except ValueError as error:
            print("There was an error with the user authentication")
            print(error)
    
    def connect_to_db(self, db_address: str):
        try:
            connect(db_address)
        except ValueError:
            print("The database address is not valid")

class AudioFile(IPlayable, IAudioConverter):
    def __init__(self, format: str):
        self.format = format
    
    def convert_audio(self, audio_format: str):
        if audio_format in VALID_AUDIO_FORMATS:
            self.format = audio_format

    @staticmethod
    def play():
        print("Playing the audio file")

class VideoFile(IPlayable, IVideoConverter):
    def __init__(self, format: str):
        self.format = format
    
    def convert_audio(self, video_format: str):
        if video_format in VALID_VIDEO_FORMATS:
            self.format = video_format

    @staticmethod
    def play():
        print("Playing the video file")




# |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
# | Dependency inversion (inyection) |
# |__________________________________|

### Violation



### Correct design



































































































# Ignore this functions, used in examples
def connect(arg):
    pass

def auth_user(arg):
    pass

VALID_AUDIO_FORMATS = ("mp3")
VALID_VIDEO_FORMATS = ("mp4")