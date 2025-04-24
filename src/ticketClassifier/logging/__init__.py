import logging
import os
import sys
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
current_date = datetime.now().strftime("%Y%m%d%H")
log_dir = "logs"
logs_path = os.path.join(log_dir, f"{current_date}.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(    
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(logs_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textClassifierLogger")