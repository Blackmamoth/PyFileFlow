from terminology import in_green, in_red, in_yellow, in_blue

class ConsoleLogger:

    @staticmethod
    def success(text: str) -> None:
        print(in_green(text))
    
    @staticmethod
    def error(text: str) -> None:
        print(in_red(text))

    @staticmethod
    def info(text: str) -> None:
        print(in_blue(text))

    @staticmethod
    def warn(text: str) -> None:
        print(in_yellow(text))