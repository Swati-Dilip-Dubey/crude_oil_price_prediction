import os
import sys
import logging

# Define format of logs
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create a sub-directory for logs in src directory.
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Define basic configurations
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # FileHandler will create a log folder
        logging.StreamHandler(sys.stdout) # StreamHandler will print in terminal
    ]
)

# Start logger
logger = logging.getLogger("mlProjectLogger")

