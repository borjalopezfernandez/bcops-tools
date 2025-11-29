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
    cmd             = f'bcops_bmpf_bct_pass --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_bct_pass --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_bct_pass --config'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_get_data(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    import importlib.resources
    import pathlib
    dist                = importlib.metadata.distribution('eocfi')
    root_dist_info      = dist._path
    dist_info_dir       = pathlib.Path(dist._path).parent
    package_root_dir    = f'{dist_info_dir}/bcops'

    file_orbsct       = f'{dist_info_dir}/bcops/data/BIO_COPS_MPL_ORBSCT'
    file_gndbct       = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_ZON_DB_00000000T000000_99999999T999999_BCT______0001.EOF'
    file_orbref       = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_ORBREF_20251121T000000_20270331T000000_0006.EOF'  
    file_swtssp       = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_SWTREF_20251121T000514_20270330T225538_GNDTRACK_0001.EOF'

    logger.info(root_dist_info)
    logger.info(dist_info_dir)
    logger.info(package_root_dir)
    logger.info(file_orbsct)
    logger.info(file_orbref)
    logger.info(file_gndbct)
    logger.info(file_swtssp)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_tom_mc1(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    # bcops_bmpf_bct_pass -s 2025-11-21T00:29:45 -e 2027-03-30T00:00:00

    cmd             = f'bcops_bmpf_bct_pass -s 2025-11-21T00:29:45 -e 2027-03-30T00:00:00 -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")