import os 
from src.datScience.entity.config_entity import DataValidationConfig
from src.datScience import logger
import pandas as pd 

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config 

    def validate_all_columns(self)->bool:
        try:
            validation_status=None

            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols=list(data.columns)

            all_schema=self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status for col names : {validation_status}")
                else:
                    validation_status=True 
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status for col names: {validation_status}")
            
                
            return validation_status


        except Exception as e:
            logger.exception(e)
            raise e
        
    def validate_data_types(self):
        try:
            validation_status=None
            data=pd.read_csv(self.config.unzip_data_dir)

            all_schema=self.config.all_schema

            for column_name,expected_dtype in all_schema.items():
                actual_dtype=str(data[column_name].dtype)
                if actual_dtype!= expected_dtype:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status for dtypes : {validation_status}")
                else:
                    validation_status=True 
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status for dtypes: {validation_status}")
            return validation_status
        except Exception as e:
            logger.exception(e)
            raise e