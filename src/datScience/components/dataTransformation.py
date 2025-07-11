import os 
from src.datScience.entity.config_entity import DataTransformationConfig
from src.datScience import logger
from sklearn.model_selection import train_test_split
import pandas as pd 


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        train,test=train_test_split(data,random_state=42)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)