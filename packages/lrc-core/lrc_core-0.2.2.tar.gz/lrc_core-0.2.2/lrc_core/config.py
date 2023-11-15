"""Config for lrc_core.
"""

import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

SMP_IP = os.getenv("SMP_IP", "172.22.246.207")
SMP_USER = os.getenv("SMP_USER", "admin")
SMP_PW = os.getenv("SMP_PW", None)

logger.debug(f"SMP_IP: {SMP_IP}, SMP_USER: {SMP_USER}")

if SMP_PW is None:
    logger.warning("No password for SMP found (in environment variables).")

EPIPHAN_URL = os.getenv("EPIPHAN_URL", "http://172.23.8.102")
EPIPHAN_USER=os.getenv("EPIPHAN_USER", "admin")
EPIPHAN_PW=os.getenv("EPIPHAN_PW", None)
