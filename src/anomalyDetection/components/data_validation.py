from anomalyDetection import logger
from pathlib import Path
import pandas as pd
import os
from anomalyDetection.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config 

    def merge_all_csv(self) -> None:
        try:
            if os.path.isfile(self.config.merged_csv_file):
                logger.info(f"Merged csv file already exists at {self.config.merged_csv_file}")
            else:
                data_dir = Path(self.config.unzip_data_dir)
                csv_files = list(data_dir.glob(r'*/*/*.csv'))
                df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)  
                df.columns = df.columns.str.strip()
                df.to_csv(self.config.merged_csv_file, index=False)
                logger.info(f"CSV files mereged and stored at {self.config.merged_csv_file}")
        except Exception as e:
            raise e

    def validate_all_columns(self) -> bool:
        try: 
            validation_status = None

            data = pd.read_csv(self.config.merged_csv_file)
            all_cols = data.columns.tolist()

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema or data[col].dtype != self.config.all_schema[col]:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e