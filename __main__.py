from helpers.options import SelectOption
from helpers.constants import Services, Operations, services

def main():
    service_option = SelectOption.choose_service()
    operation = SelectOption.choose_operation()
    service = services[service_option]
    match operation:
        case Operations.Upload.name:
            local_file_path = SelectOption.get_local_file_path()
            dropbox_file_path = SelectOption.get_remote_file_path(Services.Dropbox.name)
            overwrite = SelectOption.overwrite()
            service.upload(local_file_path, dropbox_file_path, overwrite)
        case Operations.Download.name:
            local_dir_path = SelectOption.get_local_dir_path()
            dropbox_file_path = SelectOption.get_remote_file_path(Services.Dropbox.name)
            service.download(local_dir_path, dropbox_file_path)
        case Operations.List.name:
            service.list()
            
            


main()