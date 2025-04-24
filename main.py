from ticketClassifier.logging import logger
from ticketClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<<<<<<")

    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()

    logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<< \n\n X======================================X")

except Exception as e:
    logger.exception(e)
    raise e
