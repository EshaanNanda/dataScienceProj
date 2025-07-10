from src.datScience.pipeline.dataTransformation import DataTransformationTrainingPipeline
from src.datScience import logger
from src.datScience.pipeline.dataIngestion import DataIngestionTrainingPipeline
from src.datScience.pipeline.dataValidation import DataValidationTrainingPipeline

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


STAGE_NAME="Data Validation Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx====x")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx====x")
except Exception as e:
    logger.exception(e)
    raise e