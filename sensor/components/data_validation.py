from sensor.entity import artifact_entity, config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import os,sys
import pandas as pd

class DataValidationArtifact:


    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data Validation{'>>'*20}")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SensorException(e, sys)    
        


    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        pass