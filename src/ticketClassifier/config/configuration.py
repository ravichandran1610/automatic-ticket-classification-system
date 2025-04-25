from ticketClassifier.constants import *
from ticketClassifier.utils.common import read_yaml, create_directories
from ticketClassifier.entity import (
    DataIngestionConfig,
    DataLoadConfig
)


class ConfigurationManager:
    def __init__(
            self,
            config_path = CONFIG_FILE_PATH,
            params_path = PARAMS_FILE_PATH
            ):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file
        )
        return data_ingestion_config
    
    def get_data_load_config(self) -> DataLoadConfig:
        config = self.config.data_load
        create_directories([config.root_dir])
        data_load_config = DataLoadConfig(
            root_dir=config.root_dir,
            raw_data_path=config.raw_data_path,
            df_data_path=config.df_data_path
            )
        return data_load_config
    
