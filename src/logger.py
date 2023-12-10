import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    # naming convention to be used for the log file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)    # logs will be appended to name and then the above title LOG_FILE
os.makedirs(logs_path,exist_ok=True)                 # EXIST OK TELLS EVEN IF THERE IS THAT FOLDER/FILE KEEP APENDING TO IT

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

"""
BELOW CODE IS JUST USED FOR CHECKING IF THE LOGGER.py IS WORKING PROPERLY

if __name__== "__main__":
    logging.info("LOGGER IS WORKING")

    """