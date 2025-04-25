from ticketClassifier.components.data_load import DataLoad
from ticketClassifier.config.configuration import ConfigurationManager

class DataLoadPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_load_config = config.get_data_load_config()
        data_load = DataLoad(data_load_config)
        data_load.load_data()