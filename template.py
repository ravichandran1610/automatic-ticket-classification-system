import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

projectName = "ticketClassifier"

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{projectName}/__init__.py',
    f'src/{projectName}/components/__init__.py',
    f'src/{projectName}/utils/__init__.py',
    f'src/{projectName}/utils/common.py',
    f'src/{projectName}/logging/__init__.py',
    f'src/{projectName}/pipeline/__init__.py',
    f'src/{projectName}/config/__init__.py',
    f'src/{projectName}/config/configuration.py',
    f'src/{projectName}/entity/__init__.py',
    f'src/{projectName}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'
]

for filePath in list_of_files:
    filePath = Path(filePath)
    file_dir, filename = os.path.split(filePath)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating the {file_dir} directory for {filename}")

    if not (os.path.exists(filePath)) or os.path.getsize(filePath) == 0:
        with open(filePath, 'w') as file:
            pass
        logging.info(f"{filePath} file created Successfully")
    else:
        logging.info(f"{filePath} already exists")

