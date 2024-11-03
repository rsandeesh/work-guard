import logging
import os

ENV = os.getenv("ENV", "bernie")  # default to "Production"

# Configure logger
logger = logging.getLogger("Logger")

if ENV == "development":
    logger.setLevel(logging.DEBUG)
elif ENV == "bernie":
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.INFO)

logger.propagate = False

# Create console handler and set level to debug
console_handler = logging.StreamHandler()

# log level for console handler. This will be the minimum log level that will be displayed on the console
console_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Add formatter to console handler
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)
