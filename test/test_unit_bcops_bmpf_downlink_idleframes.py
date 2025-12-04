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
    cmd             = f'bcops_bmpf_downlink_idleframes --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_downlink_idleframes --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_downlink_idleframes --list'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_bmpf_downlink_idleframes --config'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_input_errors(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_bmpf_downlink_idleframes -s 2025-10-22T00:00:00 -e 2025-10-23T00:00:00'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)

    cmd             = f'bcops_bmpf_downlink_idleframes -s 2025-10-22T00:00:00 --station-id IVK_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)
   
    cmd             = f'bcops_bmpf_downlink_idleframes -e 2025-10-22T00:00:00 --station-id IVK_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)

    cmd             = f'bcops_bmpf_downlink_idleframes -s 2025-10-22T00:00:00 -e 2025-10-23T00:00:00 --station-id IVK_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)
    
    cmd             = f'bcops_bmpf_downlink_idleframes -s 2025-10-22T00:00:00 -e 2025-10-23T00:00:00 --station-id pipo -o 38'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)

    cmd             = f'bcops_bmpf_downlink_idleframes -s 2025-10-22T00:00:00 -e 202A-10-23T00:00:00 --station-id IVK_____ -o 38'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)

    cmd             = f'bcops_bmpf_downlink_idleframes -s 2025-10-22T00:00:00 -e 2023-10-23T00:00:00 --station-id IVK_____ -o 38'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)

    cmd             = f'bcops_bmpf_downlink_idleframes -s 2025-10-22T00:00:00 -e 2027-03-30T00:00:00 --station-id IVK_____ -o 999999999'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)

    cmd             = f'bcops_bmpf_downlink_idleframes -s 2020-10-22T00:00:00 -e 2037-03-30T00:00:00 --station-id IVK_____ -o 38'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 66)

    cmd     = f'bcops_bmpf_downlink_idleframes -f test/data/BIO_OPER_MPL_XBSACQ_20251208T000000_20251214T235959_IVK______0003.EOF -o 38 --station-id IVK_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert((exit >> 8) == 99)

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
    file_orbsct         = f'{dist_info_dir}/bcops/data/BIO_COPS_MPL_ORBSCT'
    file_gnd_db         = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_GND_DB_00000000T000000_99999999T999999_STATIONS_0001.EOF'
    file_orbref         = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_ORBREF_20251121T000000_20270331T000000_0006.EOF'  
    file_swtssp         = f'{dist_info_dir}/bcops/data/BIO_OPER_MPL_SWTREF_20251121T000514_20270330T225538_GNDTRACK_0001.EOF'

    logger.info(root_dist_info)
    logger.info(dist_info_dir)
    logger.info(package_root_dir)
    logger.info(file_orbsct)
    logger.info(file_orbref)
    logger.info(file_gnd_db)
    logger.info(file_swtssp)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_parse_ppf(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    import shutil
    from lxml import etree
    
    LIST_OF_MEMORY_REQUEST  = ['DUMP_HHV', 'DUMP_HVH', 'DUMP_HK_', 'STOPDUMP', 'FREE_HK_', 'FREE_H__', 'FREE_V__'] 
    file_ppf_1_original     = f'test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF'
    file_ppf_1              = f'test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003_patched.EOF'
    shutil.copy(file_ppf_1_original, file_ppf_1)
    logger.info(file_ppf_1)
    
    station_id              = 'IVK_____'
    xml_ppf_1               = etree.parse(file_ppf_1)
    root_ppf_1              = xml_ppf_1.getroot()
    path                    = '/Earth_Explorer_File/Earth_Explorer_Header/Fixed_Header/Notes'
    fixed_header_notes      = root_ppf_1.xpath(path)
    print(fixed_header_notes)

    if len(fixed_header_notes) > 0:
        fixed_header_notes_text = fixed_header_notes[0].text

    if fixed_header_notes_text is None:
        fixed_header_notes_text = ''

    logger.debug(f"Fixed Header Notes: {fixed_header_notes_text}")
    path                    = '/Earth_Explorer_File/Data_Block/List_of_EVRQs/EVRQ'
    list_of_evrqs           = root_ppf_1.xpath(path)
    logger.debug(f"Number of EVRQs: {len(list_of_evrqs)}")
    for evrq in list_of_evrqs:
        path    = 'RQ/RQ_Name'
        rq_name = evrq.xpath(path)
        if len(rq_name) == 0:
            continue
        rq_name = rq_name[0].text
        if rq_name not in LIST_OF_MEMORY_REQUEST:
            continue
        path            = 'RQ/RQ_Absolute_orbit'
        rq_abs_orbit    = int(evrq.xpath(path)[0].text)
        print(rq_name)
        print(fixed_header_notes_text)
        print(rq_abs_orbit)

        if f'Patched passes to transmit idle frames only for {station_id}:' not in fixed_header_notes_text:
            fixed_header_notes_text += f'\nPatched passes to transmit idle frames only for {station_id}:'

        if str(rq_abs_orbit) not in fixed_header_notes_text:
            fixed_header_notes_text += f' {rq_abs_orbit}'
            
        parent = evrq.getparent()
        parent.remove(evrq)
        logger.debug(f"Number of EVRQs after removal: {len(root_ppf_1.xpath('/Earth_Explorer_File/Data_Block/List_of_EVRQs/EVRQ'))}")

    root_ppf_1.xpath('/Earth_Explorer_File/Data_Block/List_of_EVRQs')[0].set('count', str(len(root_ppf_1.xpath('/Earth_Explorer_File/Data_Block/List_of_EVRQs/EVRQ'))))
    print(fixed_header_notes_text.strip())
    fixed_header_notes[0].text = fixed_header_notes_text.strip()
    xml_ppf_1.write(file_ppf_1, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_weeklyplan(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    file_ppf_1_original     = f'test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF'
   
    for f in glob.glob('test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF_patched*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)

    cmd     = f'bcops_bmpf_downlink_idleframes -f test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF -e 2025-12-14T00:00:00 -o 38 --station-id IVK_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd     = f'bcops_bmpf_downlink_idleframes -f test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF_patched -s 2025-12-08T00:00:00 -e 2025-12-12T00:00:00 -o 38 --station-id KSE_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    '''
    
    cmd     = f'bcops_bmpf_downlink_idleframes -f test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF_patched_patched -s 2025-12-08T00:00:00 -e 2025-12-09T00:00:00 -o 38 --station-id IVK_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    # The generated file should be exactly the same as the original file
    cmd     = f'bcops_bmpf_downlink_idleframes -f test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF_patched_patched -s 2025-12-08T00:00:00 -e 2025-12-30T00:00:00 -o 38 --station-id IVK_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    '''

    for f in glob.glob('test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF_patched*'):
        logger.debug(f'Generated result file(s): {f}')

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_plan_nodates(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    file_ppf_1_original     = f'test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF'
   
    for f in glob.glob('test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF_patched*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)

    cmd     = f'bcops_bmpf_downlink_idleframes -f test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF -o 38 --station-id IVK_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd     = f'bcops_bmpf_downlink_idleframes -f test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF_patched -o 1 --station-id KSE_____'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    
    for f in glob.glob('test/data/BIO_OPER_MPL_PPF_1__20251208T000000_20251214T235959_0003.EOF_patched*'):
        logger.debug(f'Generated result file(s): {f}')

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")    