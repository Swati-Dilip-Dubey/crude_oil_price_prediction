import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        
        # Read the csv file data 
        data = pd.read_csv(self.config.data_path)
        
        # Split the data into training and test sets. (0.75, 0.25)
        train, test = train_test_split(data, test_size=0.25)

        # Save train.csv and test.csv into artifacts/data_transformation
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets.")
        logger.info(train.shape)
        logger.info(test.shape)