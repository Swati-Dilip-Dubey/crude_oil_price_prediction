import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns 

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type 
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty.")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple directories is to be created. Default to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    """load json file data 

    Args:
        path_to_json (Path): path to json file

    Raises:
        ValueError: if json file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_json, "r") as json_file:
            content = json.load(json_file)
            logger.info(f"json file {path_to_json} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("json file is empty.")
    except Exception as e:
        raise e
    
@ensure_annotations
def save_bin(path_to_binary: Path, data: Any):
    """save binary file

    Args:
        path (Path): path to binary file
        data (Any): data to be saved in binary file
    """
    joblib.dump(value=data, filename=path_to_binary)
    logger.info(f"binary file saved at {path_to_binary}")

@ensure_annotations
def load_bin(path_to_binary: Path) -> Any:
    """loads binary data 

    Args:
        path_to_binary (Path): path of binary file

    Raises:
        ValueError: if binary file is empty
        e: empty file
    
    Returns:
        Any: object stored in the file
    """
    try:
        data = joblib.load(path_to_binary)
        logger.info(f"binary file loaded from {path_to_binary}")
        return data
    except BoxValueError:
        raise ValueError("binary file is empty.")
    except Exception as e:
        raise e
    
@ensure_annotations
def get_size(path_to_file: Path) -> str:
    """Returns size of given file

    Args:
        path_to_file (Path): path of a given file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path_to_file)/1024)
    return f"~{size_in_kb} KB"