import urllib.request as request
import os
from pathlib import Path
from ticketClassifier.logging import logger
from ticketClassifier.utils.common import get_size
from ticketClassifier.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_dataset(self):
        data_file = self.config.local_data_file
        url = self.config.source_URL

        if not os.path.exists(data_file) or os.path.getsize(data_file) == 0:
            filename, header = request.urlretrieve(
                url=url,
                filename=data_file
            )
            logger.info(f"Downloaded the file successfully with the following details: {header}")
        else:
            logger.info(f"{data_file} file already exists with the size of {get_size(Path(data_file))}")
