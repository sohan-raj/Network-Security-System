from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import (DataIngestionConfig,
                                                 TrainingPipelineConfig,
                                                 DataValidationConfig,
                                                 DataTransformationConfig,
                                                 ModelTrainerConfig)
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
import sys




if __name__ == "__main__":
    try:
        TrainingPipelineConfig = TrainingPipelineConfig()
        DataIngestionConfig = DataIngestionConfig(TrainingPipelineConfig)
        data_ingestion = DataIngestion(DataIngestionConfig)
        logging.info("Initiating data ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Completed data ingestion")
        data_validataion_config = DataValidationConfig(TrainingPipelineConfig)
        
        data_validation = DataValidation(data_validataion_config,data_ingestion_artifact)
        logging.info("data validation initiated")
        data_validatioin_artifact = data_validation.initiaite_data_validation()
        logging.info("data validation completed")
        data_transformation_config = DataTransformationConfig(TrainingPipelineConfig)
        data_transformation = DataTransformation(data_validation_artifact = data_validatioin_artifact,data_transformation_config = data_transformation_config)
        logging.info("data transformation initiated")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("data transformation completed")
        
        model_trainer_config = ModelTrainerConfig(TrainingPipelineConfig)
        model_trainer = ModelTrainer(model_trainer_config,data_transformation_artifact)
        logging.info("model trainer initiated")
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("model trainer completed")
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)