from helpers.options import SelectOption
from helpers.constants import Services, Operations
from dropbox_client.service import DropboxService

def main():
    service = SelectOption.choose_service()
    operation = SelectOption.choose_operation()
    match operation:
        case Operations.Upload.name:
            local_file_path = SelectOption.get_local_file_path()
            dropbox_file_path = SelectOption.get_remote_file_path(Services.Dropbox.name)
            overwrite = SelectOption.overwrite()
            if service == Services.Dropbox.name:
                DropboxService.upload(local_file_path, dropbox_file_path, overwrite)
        case Operations.Download.name:
            local_dir_path = SelectOption.get_local_dir_path()
            dropbox_file_path = SelectOption.get_remote_file_path(Services.Dropbox.name)
            if service == Services.Dropbox.name:
                DropboxService.download(local_dir_path, dropbox_file_path)
            
            


main()