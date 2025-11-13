import sys
import os
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


def test_options(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_maap_query_datatake --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_l0_S1_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-07-22T00:00:00Z --end 2025-07-22T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_csv_l0_S1_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    import os
    import glob

    for f in glob.glob('bcops_maap_query_datatake_S1_RAW__0S_20250722T000000_20250722T020000*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-07-22T00:00:00Z --end 2025-07-22T02:00:00Z -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('bcops_maap_query_datatake_S1_RAW__0S_20250722T000000_20250722T020000*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")



def test_l1a_S1_SCS__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-07-22T00:00:00Z --end 2025-07-22T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_csv_l1a_S1_SCS__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    import os
    import glob

    for f in glob.glob('bcops_maap_query_datatake_S1_SCS__1S_20250722T000000_20250722T020000*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-07-22T00:00:00Z --end 2025-07-22T02:00:00Z -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('bcops_maap_query_datatake_S1_SCS__1S_20250722T000000_20250722T020000*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_l1b_S1_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-07-22T00:00:00Z --end 2025-07-22T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_csv_l1b_S1_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    import os
    import glob

    for f in glob.glob('bcops_maap_query_datatake_S1_DGM__1S_20250722T000000_20250722T020000*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-07-22T00:00:00Z --end 2025-07-22T02:00:00Z -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('bcops_maap_query_datatake_S1_DGM__1S_20250722T000000_20250722T020000*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")



def test_l0_S2_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_RAW__0S --start 2025-10-22T00:00:00Z --end 2025-10-22T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_l1a_S2_SCS__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_SCS__1S --start 2025-10-22T00:00:00Z --end 2025-10-22T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_l1b_S2_DGM__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_DGM__1S --start 2025-10-22T00:00:00Z --end 2025-10-22T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_l0_S3_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_RAW__0S --start 2025-11-04T00:00:00Z --end 2025-11-04T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_l1a_S3_SCS__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_SCS__1S --start 2025-11-04T00:00:00Z --end 2025-11-04T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_l1b_S3_DGM__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_DGM__1S --start 2025-11-04T00:00:00Z --end 2025-11-04T02:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")