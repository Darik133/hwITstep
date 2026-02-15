import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    filemode='w',
    format="Your program successfully launch: %(asctime)s, %(levelname)s, %(message)s"
)

current_date = datetime.now().strftime("%Y-%m-%d")

logging.info(f"Current date: {current_date}")
