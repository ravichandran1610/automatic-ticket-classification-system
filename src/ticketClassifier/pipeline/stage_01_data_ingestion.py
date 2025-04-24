from ticketClassifier.config.configuration import ConfigurationManager
from ticketClassifier.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)

        data_ingestion.download_dataset()