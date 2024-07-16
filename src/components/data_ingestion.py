import os
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path
from src.entity.config_entity import DataIngestionConfig
from src import logger
from src.utils import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started...")
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")        

    def unzip_file(self):
        
        if not os.path.exists(self.config.local_data_file):
            os.makedirs(self.config.unzip_dir)
        
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            print(f"Files extracted to {self.config.unzip_dir}")
            logger.info(f"Files extracted to {self.config.unzip_dir}")