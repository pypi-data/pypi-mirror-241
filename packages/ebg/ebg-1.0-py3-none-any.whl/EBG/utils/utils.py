import logging
import os
import subprocess

from EBG.Models.get_model import get_model


def setup_logger(instance_name):
    logger = logging.getLogger(instance_name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger


def load_model(name):
    return get_model(name)


def check_file_exists(file_path, file_description):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_description} not found: {file_path}")


def check_raxml_availability():
    if os.name == "posix":
        return subprocess.check_output(["which", "raxml-ng"], text=True).strip()
    elif os.name == "nt":
        return subprocess.check_output(["gcm", "raxml-ng"], text=True).strip()


def format_predictions(predictions):
    predictions = [0 if x < 0 else x for x in predictions]
    predictions = [100 if x > 100 else x for x in predictions]
    int_predictions = [int(value) for value in predictions]
    return int_predictions
