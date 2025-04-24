import yaml
import os
from ticketClassifier.logging import logger
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path


@ensure_annotations
def read_yaml(filePath: Path) -> ConfigBox:
    try:
        with open(filePath, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file loaded successfully: {filePath}")
            return ConfigBox(config)
            
    except BoxValueError:
        raise ValueError(f"YAML file is empty: {filePath}")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(folder_list:list, verbose=True):
    for folderPath in folder_list:
        os.makedirs(folderPath, exist_ok=True)    
        if verbose:
            logger.info(f"Create the directory: {folderPath}")


@ensure_annotations
def get_size(filePath:Path) -> str:
    size_in_kb = round(os.path.getsize(filePath)/1024)
    return f"{size_in_kb} KB"
