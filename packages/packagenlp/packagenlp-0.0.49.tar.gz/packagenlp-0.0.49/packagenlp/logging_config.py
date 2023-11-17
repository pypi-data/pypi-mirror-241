import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    log_directory = os.path.join(os.getcwd(), 'log')
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file_path = os.path.join(log_directory, 'nlp.log')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)',
        handlers=[
            RotatingFileHandler(log_file_path, maxBytes=5*1024*1024, backupCount=3),
            logging.StreamHandler()
        ]
    )
