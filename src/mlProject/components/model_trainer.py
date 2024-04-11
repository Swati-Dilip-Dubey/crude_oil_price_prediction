import os
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig
from mlProject import logger

class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def train(self) -> None:

        # 
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Drop the Target Column
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)

        # Assign the label
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Model creation
        model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )

        # Train the model
        model.fit(train_x, train_y)

        # Save the trained model
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))