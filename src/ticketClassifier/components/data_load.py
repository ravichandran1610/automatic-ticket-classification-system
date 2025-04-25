from ticketClassifier.config.configuration import DataLoadConfig
from ticketClassifier.logging import logger
import json
import pandas as pd
import os

class DataLoad:
    def __init__(self, config:DataLoadConfig):
        self.config = config
    
    def load_data(self):
        if not os.path.exists(self.config.df_data_path) or os.path.getsize(self.config.df_data_path)==0:
            json_file = open(self.config.raw_data_path, 'r')
            print(json_file)
            json_data = json.load(json_file)
            df = pd.json_normalize(json_data)
            df.to_pickle(self.config.df_data_path)
            logger.info(f"Loaded raw JSOn and created Dataframe: {self.config.df_data_path}")
        else:
            logger.info(f"The Dataframe file already exist: {self.config.df_data_path}")
