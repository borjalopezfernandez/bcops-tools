import sys
import os
import shutil
import pathlib
import glob
import time
import pytest
from importlib.metadata import version

from loguru import logger


@pytest.fixture(scope = "function", autouse = True)
def test_setup():
    logger.info('test')
    logger.info('----------------- test_setup() -------------------')


@pytest.fixture
def print_separator():
    logger.debug("\n=========================================================================")


def test_datetime_relative_orbit(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd = f'bcops_eocfi_time_relative_orbit -t 20261022T000000'
    logger.info(cmd)
    exit = os.system(cmd)
    assert( exit >> 8 == 0 )
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")