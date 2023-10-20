from anomalyDetection import logger
from anomalyDetection.pipeline.stage_01_data_ingestation import DataIngestionPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<\n\nx=======================x")
except Exception as e:
    logger.exception(e)
    raise e