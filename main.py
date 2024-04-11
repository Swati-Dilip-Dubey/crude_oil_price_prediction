from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

# # Check for custom log. This will be printed everytime when main.py will be executed.
# logger.info("Welcome to our custom log.")

# Data Ingestion stage
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e


# Data Validation stage
STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e

# Data Transformation stage
STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e


# Model Trainer stage
STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e