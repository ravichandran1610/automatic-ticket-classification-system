from ticketClassifier.logging import logger
from ticketClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from ticketClassifier.pipeline.stage_02_data_load import DataLoadPipeline
from ticketClassifier.logging import logger

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<< \n\n X======================================X")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Loading"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<<<<<<")
    data_load_pipeline = DataLoadPipeline()
    data_load_pipeline.main()
    logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<< \n\n X======================================X")
except Exception as e:
    logger.exception(e)
    raise e
