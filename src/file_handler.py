import json
from src.logger import logger

def read_json(filepath):
    """Reads JSON data from a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(f"Successfully read data from {filepath}")
            return data
    except FileNotFoundError:
        logger.error(f"File '{filepath}' not found. Returning empty data.")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format in '{filepath}'. Returning empty data.")
    
    return []

def write_json(filepath, data):
    """Writes JSON data to a file."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        logger.info(f"Successfully wrote transformed data to {filepath}")
    except Exception as e:
        logger.error(f"Error writing to file '{filepath}': {e}")