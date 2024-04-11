from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline 
from mlProject.pipeline.stage_05_model_evaluation import  ModelEvaluationTrainingPipeline

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


STAGE_NAME4 = "Model Trainer stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME4} started <<<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME4} completed <<<<<<<< \n\n x=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME5 = "Model Evaluation stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME5} started <<<<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME5} completed <<<<<<<< \n\n x=============x")
except Exception as e:
    logger.exception(e)
    raise e
