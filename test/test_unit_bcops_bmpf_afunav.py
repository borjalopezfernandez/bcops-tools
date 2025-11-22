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
    cmd             = f'bcops_bmpf_afunav --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_afunav --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_afunav --list'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_afunav --config'
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
    file_gnd_db       = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_GND_DB_00000000T000000_99999999T999999_STATIONS_0001.EOF'
    file_orbref       = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_ORBREF_20251121T000000_20270331T000000_0006.EOF'  
    file_swtssp       = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_SWTREF_20251121T000514_20270330T225538_GNDTRACK_0001.EOF'

    logger.info(root_dist_info)
    logger.info(dist_info_dir)
    logger.info(package_root_dir)
    logger.info(file_orbsct)
    logger.info(file_orbref)
    logger.info(file_gnd_db)
    logger.info(file_swtssp)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_errors(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    
    # non existing station id
    cmd             = f'bcops_bmpf_afunav -s 2025-10-22T00:00:00 -e 2025-10-23T00:00:00 -o 65 --station-id S1'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit != 0)


def test_tom_mc1(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    # eocfi_vistime_station --file-orbit src/bcops/data/BIO_OPER_MPL_ORBREF_20251121T000000_20270331T000000_0006.EOF --file-swath src/bcops/data/BIO_OPER_MPL_SWTREF_20251121T000514_20270330T225538_GNDTRACK_0001.EOF --file-station src/bcops/data/BIO_OPER_MPL_GND_DB_00000000T000000_99999999T999999_STATIONS_0001.EOF --station-id IVK_____ --time-start 9560 --time-end 9561

    # bcops_bmpf_afunav -s 2025-11-25T00:00:00 -e 2025-11-30T00:00:00 -o 38 --station-id IVK_____

    # Inuvik station id

    for f in glob.glob('BIO_OPER_MPL_AFUNAV*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)

    cmd             = f'bcops_bmpf_afunav -s 2025-11-25T00:00:00 -e 2025-11-30T00:00:00 -o 38 --station-id IVK_____ -D'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    # eocfi_validate_xml -s ../pyeocfi/schemas/bmpf/EO_OPER_MPL_AFUNAV_0100.XSD -f BIO_OPER_MPL_AFUNAV_20251126T125052_20251126T130356_IVK______0001.EOF

    assert(len(glob.glob('BIO_OPER_MPL_AFUNAV*')) != 0)

    for f in glob.glob('BIO_OPER_MPL_AFUNAV*'):
        logger.debug(f'Generated result file: {f}')

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")