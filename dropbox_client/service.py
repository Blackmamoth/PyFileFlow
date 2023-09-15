from helpers.environment import Environment
from helpers.filesystem import Filesystem
from helpers.console import ConsoleLogger
from dropbox import Dropbox, files
from dropbox.exceptions import AuthError
from prettytable import PrettyTable


class DropboxService:

    client = Dropbox(
                app_key=Environment.DROPBOX_APP_KEY,
                app_secret=Environment.DROPBOX_APP_SECRET,
                oauth2_access_token=Environment.DROPBOX_ACCESS_TOKEN
            )

    @staticmethod
    def upload(local_file_path: str, dropbox_file_path: str,overwrite=False) -> bool:
        try:
            if not Filesystem.check_file_exists(local_file_path):
                return False
            with open(local_file_path, "rb") as f:
                file_data = f.read()
                mode = files.WriteMode.overwrite if overwrite else files.WriteMode.add
                DropboxService.client.files_upload(file_data, dropbox_file_path, mode)
                ConsoleLogger.success('File upload successful')
                return False
        except AuthError as e:
            ConsoleLogger.error(e.error)
            return False
        except Exception as e:
            ConsoleLogger.error(e)
            return False
        
    @staticmethod
    def download(local_dir_path: str, dropbox_file_path: str) -> bool:
        try:
            Filesystem.create_dir(local_dir_path)
            metadata, result = DropboxService.client.files_download(path=dropbox_file_path)
            file_path = Filesystem.create_file_path(local_dir_path, metadata.name)
            with open(file_path, 'wb') as f:
                f.write(result.content)
                ConsoleLogger.info('File download.')
                return True
        except Exception as e:
            ConsoleLogger.error(e)
            return False
        
    @staticmethod
    def list() -> None:
        try:
            files_data = DropboxService.client.files_list_folder('/').entries
            ptable = PrettyTable()
            ptable.field_names = ['Name', 'Path', 'Size']
            for file in files_data:
                if isinstance(file, files.FileMetadata):
                    ptable.add_row([file.name, file.path_display, f'{round(file.size / 1024000, 2)} MB'])
            print(ptable)
            
        except Exception as e:
            ConsoleLogger.error(e)
