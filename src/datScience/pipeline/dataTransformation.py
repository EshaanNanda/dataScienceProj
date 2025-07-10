from src.datScience.pipeline.dataValidation import DataValidationTrainingPipeline
from src.datScience.config.configuration import ConfigurationManager
from src.datScience.components.dataTransformation import DataTransformation
from src.datScience import logger
from pathlib import Path
STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:raise Exception("Your data scheme is not valid")

        except Exception as e:
            print(e)


if __name__=="__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started <<<")
        obj=DataValidationTrainingPipeline()
        obj.initiate_data_vtransformation
        logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e