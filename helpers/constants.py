from enum import Enum

class Services(Enum):
    Dropbox = "Dropbox"
    GDrive = "GDrive"

class Operations(Enum):
    Upload = "Upload"
    Download = "Download"
    List = "List"

