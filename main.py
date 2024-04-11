from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME1 = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME1} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME1} completed <<<<<<<< \n\n x=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME2 = "Data Validation stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME2} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME2} completed <<<<<<<< \n\n x=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME3 = "Data Transformation stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME3} started <<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME3} completed <<<<<<<< \n\n x=============x")
except Exception as e:
    logger.exception(e)
    raise e