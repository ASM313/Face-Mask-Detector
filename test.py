from src import logging
from src.utils.common import read_yaml
from src.config.gcloud_syncer import GCloudSync

if __name__=="__main__":
    logging.info("Asslamu alaikum")
    # read_yaml('H:\mask detector\Face-Mask-Detector\params.yaml')
    obj=GCloudSync()
    obj.sync_folder_from_gcloud("masked_data", "mask_data.zip", "artifacts\data_ingestion")
    