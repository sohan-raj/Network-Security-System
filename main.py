from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.components.data_validation import DataValidation
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
        logging.info("data validation initiaded")
        data_validatioin_artifact = data_validation.initiaite_data_validation()
        logging.info("data validation completed")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)