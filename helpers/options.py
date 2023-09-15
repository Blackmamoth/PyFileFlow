from helpers.constants import Services, Operations
import inquirer

class SelectOption:

    @staticmethod
    def choose_service() -> str:
        services = [
            inquirer.List('service',
                        message='Choose a service',
                        choices=[Services.Dropbox.name, Services.GDrive.name]
                        )
        ]
        service = inquirer.prompt(services).get('service')
        return service
    
    @staticmethod
    def choose_operation() -> str:
        operations = [
            inquirer.List('operation',
                        message='Choose an operation',
                        choices=[Operations.Upload.name, Operations.Download.name, Operations.List.name]
                        )
        ]
        operation = inquirer.prompt(operations).get('operation')
        return operation
    
    @staticmethod
    def get_local_file_path(exists: bool = True) -> str:
        file_path = [
            inquirer.Path('local_file_path',
                        message='Enter path to your local file', 
                        path_type=inquirer.Path.FILE, exists=exists)
        ]
        local_file_path = inquirer.prompt(file_path).get('local_file_path')
        return local_file_path
    
    @staticmethod
    def get_local_dir_path(exists: bool = True) -> str:
        dir_path = [
            inquirer.Path('local_dir_path',
                        message='Enter path to your local dir', 
                        path_type=inquirer.Path.DIRECTORY, exists=exists)
        ]
        local_dir_path = inquirer.prompt(dir_path).get('local_dir_path')
        return local_dir_path

    @staticmethod
    def get_remote_file_path(service: str) -> str:
        file_path = [
            inquirer.Path('remote_file_path', 
                        message=f'Enter path to file uploaded on {service.lower()}', 
                        path_type=inquirer.Path.FILE)
        ]
        remote_file_path = inquirer.prompt(file_path).get('remote_file_path')
        return remote_file_path
    
    @staticmethod
    def overwrite() -> bool:
        print('Overwrite if file already exists')
        overwrite = [
            inquirer.Confirm('overwrite')
        ]
        overwrite = inquirer.prompt(overwrite).get('overwrite')
        return overwrite
    
    