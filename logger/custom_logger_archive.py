import os
import logging
from datetime import datetime
import structlog
class CustomLoggerArchive: # good for development purposes but format is not suitable for production
    def __init__(self,log_dir="logs"):
        # Ensure logs directory exists, if not -> create it
        self.logs_dir = os.path.join(os.getcwd(), log_dir) # log directory created at current root directory
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create timestamped log file name
        log_file = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
        log_file_path = os.path.join(self.logs_dir, log_file)

        # Configure logging -> format and level of importance to log
        logging.basicConfig(
            filename=log_file_path,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )
        
    def get_logger(self,name=__file__):
        return logging.getLogger(os.path.basename(name))
if __name__ == "__main__":
    logger = CustomLoggerArchive()
    logger=logger.get_logger(__file__)
    logger.info("Custom logger initialized.")