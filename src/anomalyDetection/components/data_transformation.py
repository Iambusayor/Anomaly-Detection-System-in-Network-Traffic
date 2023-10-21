import os
from anomalyDetection import logger
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from anomalyDetection.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def preprocess_data(self):
        """
        Preprocess steps;
            - drop missing values (nan, -inf, inf)
            - encode categorical variables
        """
        # missing values
        df = pd.read_csv(self.config.data_path)
        logger.info(f"Shape before removing inf, -inf values and nan values: {df.shape}")
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        df.drop_duplicates(keep="first", inplace=True)
        logger.info(f"Shape after removing duplicates, inf, -inf values and nan values: {df.shape}")
        # encode categorical variables
        df.Label.replace("Web.*", "Web Attack", regex=True, inplace=True)
        df.Label.replace(r'.*Patator$', "Brute Force", regex=True,inplace=True)
        df.Label.replace(["DoS GoldenEye", "DoS Hulk", "DoS Slowhttptest", "DoS slowloris"], "DoS", inplace=True)
        df.Label.replace(["DoS", "PortScan", "DDoS", "Brute Force", "Web Attack", "Bot", "Infiltration", "Heartbleed"], "Attack", inplace=True)
        df.Label.replace("BENIGN", "Normal", inplace=True)
        logger.info(f"The target labels are:  {df.Label.unique().tolist()}")
        df.Label.replace({"Normal": 1, "Attack": -1}, inplace=True)
        df.to_csv(self.config.preprocessed_data, index=False)

    def split_data(self):
        data = pd.read_csv(self.config.preprocessed_data)

        logger.info("Splitting data...")
        train_data, test_data = train_test_split(data, random_state=42, shuffle=True)

        train_data.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test_data.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info(f"Train shape: {train_data.shape}")
        logger.info(f"test shape: {test_data.shape}")