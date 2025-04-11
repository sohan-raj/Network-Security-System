from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
# from networksecurity.entity.artifact_entity import DataIngestionArtifact

import sys




if __name__ == "__main__":
    try:
        TrainingPipelineConfig = TrainingPipelineConfig()
        DataIngestionConfig = DataIngestionConfig(TrainingPipelineConfig)
        data_ingestion = DataIngestion(DataIngestionConfig)
        logging.info("Initiating data ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
        logging.info("Completed data ingestion")
    except Exception as e:
        raise NetworkSecurityException(e,sys)