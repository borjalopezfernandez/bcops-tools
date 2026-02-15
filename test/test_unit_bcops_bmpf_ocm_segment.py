import sys
import os
import glob
import time
import pytest
from importlib.metadata import version

from loguru import logger


@pytest.fixture(scope = "function", autouse = True)
def test_setup():
    logger.info('test')
    logger.info('----------------- test_setup() -------------------')


@pytest.fixture(scope = "function", autouse = True)
def check_eocfi():
    logger.info('check_eocfi')
    try:
        import eocfi
    except:
        logger.error("eocfi package not available")
        logger.info(f'get eocfi at https://eop-cfi.esa.int/index.php/mission-cfi-software/eocfi-software')
        pytest.fail("eocfi package not available")


@pytest.fixture
def print_separator():
    logger.debug("\n=========================================================================")


def test_options(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_bmpf_ocm_segment --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_ocm_segment --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_ocm_segment --config'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_tom_mc1(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_bmpf_ocm_segment -s 2025-11-21T00:29:45 -e 2027-03-30T00:00:00'
    logger.info(cmd)
    exit = os.system(cmd)
    assert( exit >> 8 == 0 )
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")