from src.datScience import logger
from src.datScience.pipeline.dataIngestion import DataIngestionTrainingPipeline

logger.info("Welcome to our cutsom logging dataScience")

STAGE_NAME=" Data Ingestion stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx====x")
except Exception as e:
    logger.exception(e)
    raise e