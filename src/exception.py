import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,tb = error_detail.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    error_message= "error occured at line number: "+str(tb.tb_lineno)
    file_name,tb.tb_lineno,str(error)
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        self.error_message = error_message
        super().__init__(self.error_message)
        self.error_detail = error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message + " " + self.error_detail
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("This is a test log message")
        raise CustomException(e,sys)