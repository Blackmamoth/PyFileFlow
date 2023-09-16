from enum import Enum
from dropbox_client.service import DropboxService

class Services(Enum):
    Dropbox = "Dropbox"
    GDrive = "GDrive"

class Operations(Enum):
    Upload = "Upload"
    Download = "Download"
    List = "List"

services = {
    Services.Dropbox.name: DropboxService
}