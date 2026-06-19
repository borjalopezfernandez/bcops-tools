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


def test_COM_S1_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-05-22T09:00:00Z --end 2025-10-06T20:51:53Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM_S1_SCS__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-05-22T09:00:00Z --end 2025-10-06T20:51:53Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM0_S1_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-05-19T00:00:00Z --end 2025-06-05T20:51:57Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM0_S1_SCS__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-05-19T00:00:00Z --end 2025-06-05T20:51:57Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")



def test_COM1_S1_RAW__0S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-06-05T20:51:57Z --end 2025-06-23T20:51:57Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM1_S1_RAW__0S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-06-05T20:51:57Z --end 2025-06-23T20:51:57Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM1_S1_SCS__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-06-05T20:51:57Z --end 2025-06-23T20:51:57Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM1_S1_SCS__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-06-05T20:51:57Z --end 2025-06-23T20:51:57Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM1_S1_DGM__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-06-05T20:51:57Z --end 2025-06-23T20:51:57Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM1_S1_DGM__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-06-05T20:51:57Z --end 2025-06-23T20:51:57Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")



def test_COM2_S1_RAW__0S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-07-02T20:51:57Z --end 2025-08-31T20:54:02Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM2_S1_RAW__0S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-07-02T20:51:57Z --end 2025-08-31T20:54:02Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM2_S1_SCS__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-07-02T20:51:57Z --end 2025-08-31T20:54:02Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM2_S1_SCS__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-07-02T20:51:57Z --end 2025-08-31T20:54:02Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM2_S1_DGM__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-07-02T20:51:57Z --end 2025-08-31T20:54:02Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM2_S1_DGM__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-07-02T20:51:57Z --end 2025-08-31T20:54:02Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM3_S1_RAW__0S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-09-09T20:53:59Z --end 2025-10-03T20:51:55Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM3_S1_RAW__0S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-09-09T20:53:59Z --end 2025-10-03T20:51:55Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM3_S1_SCS__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-09-09T20:53:59Z --end 2025-10-03T20:51:55Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM3_S1_SCS__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-09-09T20:53:59Z --end 2025-10-03T20:51:55Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM3_S1_DGM__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-09-09T20:53:59Z --end 2025-10-03T20:51:55Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM3_S1_DGM__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-09-09T20:53:59Z --end 2025-10-03T20:51:55Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM4_S2_RAW__0S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_RAW__0S --start 2025-10-06T20:51:53Z --end 2025-11-02T00:29:58Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM4_S2_RAW__0S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_RAW__0S --start 2025-10-06T20:51:53Z --end 2025-11-02T00:29:58Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM4_S2_SCS__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_SCS__1S --start 2025-10-06T20:51:53Z --end 2025-11-02T00:29:58Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM4_S2_SCS__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_SCS__1S --start 2025-10-06T20:51:53Z --end 2025-11-02T00:29:58Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM4_S2_DGM__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_DGM__1S --start 2025-10-06T20:51:53Z --end 2025-11-02T00:29:58Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM4_S2_DGM__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_DGM__1S --start 2025-10-06T20:51:53Z --end 2025-11-02T00:29:58Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM5_S3_RAW__0S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_RAW__0S --start 2025-11-02T20:48:54Z --end 2025-11-21T00:29:58Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM5_S3_RAW__0S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_RAW__0S --start 2025-11-02T20:48:54Z --end 2025-11-21T00:29:58Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM5_S3_SCS__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_SCS__1S --start 2025-11-02T20:48:54Z --end 2025-11-21T00:29:58Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM5_S3_SCS__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_SCS__1S --start 2025-11-02T20:48:54Z --end 2025-11-21T00:29:58Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM5_S3_DGM__1S_B01(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_DGM__1S --start 2025-11-02T20:48:54Z --end 2025-11-21T00:29:58Z --baseline 01 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_COM5_S3_DGM__1S_B02(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_DGM__1S --start 2025-11-02T20:48:54Z --end 2025-11-21T00:29:58Z --baseline 02 -D -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S1_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_csv_TOM_GC1_MC1_S1_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    import os
    import glob

    for f in glob.glob('bcops_maap_query_datatake_S1_RAW__0S_20251121T002945_20251212T002958*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'bcops_maap_query_datatake --type S1_RAW__0S --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z -C'
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



def test_TOM_GC1_MC1_S1_SCS__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_csv_TOM_GC1_MC1_S1_SCS__1S(print_separator):
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
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('bcops_maap_query_datatake_S1_SCS__1S_20251121T002945_20251212T002958*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S1_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_csv_TOM_GC1_MC1_S1_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    import os
    import glob

    for f in glob.glob('bcops_maap_query_datatake_S1_DGM__1S_20251121T002945_20251212T002958*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('bcops_maap_query_datatake_S1_DGM__1S_20251121T002945_20251212T002958*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


# PDGS-OPS-GEN-03
# From L1a SCS to L1c STA Products Generation
'''
PDGS-CPF starts the L1c Stack generation providing, to the Stack processor, a set of L1 SCS
products (Sx_SCS__1S) having the same values of:
• Mission Phase ID
• Global Coverage ID
• Major Cycle ID
• Swath ID
• Track Number
• Frame Number
'''

def test_TOM_GC1_MC1_S1_STA__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_STA__1S --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S2_SCS__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_SCS__1S --start 2025-12-12T00:29:58Z --end 2026-01-02T00:30:12Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S2_STA__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_STA__1S --start 2025-12-12T00:29:58Z --end 2026-01-12T00:30:12Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S3_STA__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_STA__1S --start 2026-01-12T00:30:12Z --end 2026-02-01T00:30:31Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S1_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S2_RAW__0S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_RAW__0S --start 2025-12-12T00:29:58Z --end 2026-01-02T00:30:12Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S2_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_DGM__1S --start 2025-12-12T00:29:58Z --end 2026-01-02T00:30:12Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S1_AUX_TEC(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd  = f'bcops_maap_query_datatake --type AUX_TEC___ --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z -C -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S1_AUX_ERP_RD(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd  = f'bcops_maap_query_datatake --type AUX_ERP_RD --start 2025-11-21T00:29:45Z --end 2025-12-12T00:29:58Z -C -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC2_S3_SCS__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_SCS__1S --start 2026-03-24T00:34:57Z --end 2026-04-14T00:35:10Z -D -C > TOM_GC1_MC2_S3_SCS__1S.datatakes'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC2_S3_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S3_DGM__1S --start 2026-03-24T00:34:57Z --end 2026-04-14T00:35:10Z -D -C > TOM_GC1_MC2_S3_DGM__1S.datatakes'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")    


def test_TOM_GC1_MC3_S1_SCS__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_SCS__1S --start 2026-04-23T00:39:09Z --end 2026-05-14T00:39:22Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC3_S1_STA__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_STA__1S --start 2026-04-23T00:39:09Z --end 2026-05-14T00:39:22Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC3_S1_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S1_DGM__1S --start 2026-04-23T00:39:09Z --end 2026-05-14T00:39:22Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC3_S2_SCS__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_SCS__1S --start 2026-05-14T00:39:22Z --end 2026-06-04T00:39:36Z -D -C > TOM_GC1_MC3_S2_SCS__1S.datatakes'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC3_S2_DGM__1S(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type S2_DGM__1S --start 2026-05-14T00:39:22Z --end 2026-06-04T00:39:36Z -D -C > TOM_GC1_MC3_S2_DGM__1S.datatakes'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")




def test_TOM_GC1_MC1_S2_AUX_TEC(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd  = f'bcops_maap_query_datatake --type AUX_TEC___ --start 2025-12-12T00:29:58Z --end 2026-01-02T00:30:12Z -C -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC1_S2_AUX_ERP_RD(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd  = f'bcops_maap_query_datatake --type AUX_ERP_RD --start 2025-12-12T00:29:58Z --end 2026-01-02T00:30:12Z -C -D'
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


def test_TOM_GC1_MC3_FP_FD__L2A(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type FP_FD__L2A  --type FP_FD__L2A --start 2026-04-26T20:48:54Z --end 2026-04-26T20:49:58Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC3_FP_GN__L2A(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type FP_GN__L2A  --type FP_GN__L2A --start 2026-04-26T20:48:54Z --end 2026-04-26T20:49:58Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_TOM_GC1_MC3_FP_FH__L2A(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_datatake --type FP_FH__L2A  --type FP_FH__L2A --start 2026-04-26T20:48:54Z --end 2026-04-26T20:49:58Z -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")