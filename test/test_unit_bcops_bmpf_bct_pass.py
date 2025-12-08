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


def test_parse_mission_timeline(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    import importlib.resources
    import pathlib
    dist                = importlib.metadata.distribution('bcops')
    root_dist_info      = dist._path
    dist_info_dir       = pathlib.Path(dist._path).parent
    package_root_dir    = f'{dist_info_dir}/bcops'
    file_misstl         = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_MISSTL_20251121T002945_20270331T003349_TOM______0001.EOF'
    logger.info(file_misstl)

    from lxml import etree
    from datetime import datetime

    xml_file    = None
    xml_root    = None

    try:
        xml_file = etree.parse(file_misstl)
        xml_root = xml_file.getroot() 
    except:
        logger.error('Error parsing')
    
    path = '/Earth_Explorer_File/Data_Block/List_of_Global_Coverages/Global_Coverage/List_of_Major_Cycles/Major_Cycle'

    list_major_cycle = xml_root.xpath(path)

    for major_cycle in list_major_cycle:
        print(major_cycle.tag)
        print(major_cycle.attrib)
        print(major_cycle.attrib['id'])

    print()
    path = '/Earth_Explorer_File/Data_Block/List_of_Global_Coverages/Global_Coverage/List_of_Major_Cycles/Major_Cycle/List_of_Swaths/Swath'

    list_xml_swath  = xml_root.xpath(path)
    date_format     = 'UTC=%Y-%m-%dT%H:%M:%S'
    list_swath      = []

    for xml_swath in list_xml_swath:
        swath               = {}
        swath_start         = datetime.strptime(xml_swath.xpath('Start_Time')[0].text, date_format)
        swath_stop          = datetime.strptime(xml_swath.xpath('Stop_Time')[0].text, date_format)
        swath['id']         = xml_swath.attrib['id']
        swath['Start_Time'] = swath_start
        swath['Stop_Time']  = swath_stop
        print(swath['id'])
        print(swath_start)
        print(swath_stop)
        list_swath.append(swath)
        
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_parser_mission_timeline(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    import bcops.bcops_bmpf_parse_misstl as parser_misstl
    import importlib
    import pathlib
    dist            = importlib.metadata.distribution('bcops')
    dist_info_dir   = pathlib.Path(dist._path).parent
    file_misstl     = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_MISSTL_20251121T002945_20270331T003349_TOM______0001.EOF'
    list_swath      = parser_misstl.parse_mission_timeline_swath_cycle(file_misstl, logger, debug = True)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")



def test_tom_mc1(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_bmpf_bct_pass -s 2025-11-21T00:29:45 -e 2027-03-30T00:00:00'
    logger.info(cmd)
    exit = os.system(cmd)
    assert( exit >> 8 == 0 )
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")
