import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str , error_detail: sys) -> None:
        self.message = error_message
        _,_, exc_tb = error_detail.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self) -> str:
        return f"Error occured in python script name [{self.filename}] line number [{self.lineno}] error message [{self.message}]"


    
