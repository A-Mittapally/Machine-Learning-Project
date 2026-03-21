import sys 
import logging
import os
from datetime import datetime
from Source.logger import logging

# -------------------- LOGGER SETUP --------------------
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)

# -------------------- EXCEPTION HANDLING --------------------
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


# -------------------- TEST --------------------
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        error = CustomException(e, sys)
        logging.error(str(error))
        logging.shutdown()
        print(f"Log saved to: {LOG_FILE_PATH}")
        raise error