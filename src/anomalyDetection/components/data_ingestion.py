import os
import opendatasets as od
import zipfile
from anomalyDetection.entity.config_entity import DataIngestionConfig  
from anomalyDetection import logger
from anomalyDetection.utils.common import get_size
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) #TODO: Fix environment variables for kaggle api



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_files(self):
        if not os.path.exists(self.config.local_data_file):
            os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
            os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')
            api = KaggleApi()
            api.authenticate()
            api.dataset_download_files(
                self.config.dataset_ID,
                path=self.config.local_data_file,
                unzip=True
            )
            logger.info(f"{self.config.dataset_ID.split('/')[-1]} downloaded to {self.config.local_data_file}")
            logger.info(f"File size: {get_size(Path(self.config.local_data_file))}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts rge zip file into the directory
        Function returns None
        """

        os.makedirs(self.config.unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
