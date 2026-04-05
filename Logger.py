from enum import Enum

class LoggerType(Enum):
    SUCCESS = 0
    REGULAR = 1
    WARNING = 2
    ERROR = 3

def custom_print(content: str, logger_type: LoggerType):
    if logger_type == LoggerType.WARNING:
        print(f"\033[33m>> {content}\033[0m")  # Yellow text for warnings
    elif logger_type == LoggerType.ERROR:
        print(f"\033[31m>> {content}\033[0m")  # Red text for errors
    elif logger_type == LoggerType.SUCCESS:
        print(f"\033[32m>> {content}\033[0m")  # Green text for success messages
    else:
        print(f">> {content}")
