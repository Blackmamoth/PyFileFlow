from pathlib import Path
from helpers.console import ConsoleLogger

class Filesystem:

    @staticmethod
    def check_file_exists(file_path: str) -> bool:
        file_obj = Path(file_path)
        if not file_obj.exists():
            ConsoleLogger.error(f'Path {file_path} does not exist.')
            return False
        if not file_obj.is_file():
            ConsoleLogger.error(f'{file_obj.name} is not a file.')
            return False
        return True
    
    @staticmethod
    def create_dir(dir_path: str) -> None:
        try:
            dir_path_exists = Path(dir_path).exists()
            if not dir_path_exists:
                Path(dir_path).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            ConsoleLogger.error(e)

    @staticmethod
    def create_file_path(dir_path: str, file_name: str) -> str:
        return Path(dir_path).joinpath(file_name)


