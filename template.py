import os
from pathlib import Path
import logging

# Configure logging with the desired format and level
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name: str = 'anomalyDetection'

# List of files and directories to be created
list_of_files: list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

# Iterate through the list of files
for filepath in list_of_files:
    path: Path = Path(filepath)  # Convert filepath to Path object for better path handling
    filedir: str
    filename: str
    filedir, filename = os.path.split(filepath)  # Split filepath into directory and filename

    # Check if a directory path is present, and create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # exist_ok=True ensures no error if directory already exists
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if the file exists and is not empty, otherwise create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:  # Open file for writing, creating it if it doesn't exist
            pass  # 'pass' is a no-operation statement in Python
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists!")  # Log if the file already exists and is not empty
