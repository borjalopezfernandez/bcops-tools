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
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_product --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'bcops_maap_query_product --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_bio_s2_raw__0s(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_product --id BIO_S2_RAW__0S_20251020T064818_20251020T065015_C_G___M___C___T____F047_01_DGSWJK | jq .properties.updated,.properties.created,.properties.start_datetime,.properties.end_datetime'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_bio_aux_att(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_product --id BIO_AUX_ATT____20251212T133811_20251212T135348_01_DJJXAJ | jq .properties.updated,.properties.created,.properties.start_datetime,.properties.end_datetime'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_bio_mpl_orbpre(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_product --id BIO_OPER_MPL_ORBPRE_20250509T000000_20250523T000000_0001 | jq .properties.updated,.properties.created,.properties.start_datetime,.properties.end_datetime'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_bio_aux_tec(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_maap_query_product --id BIO_AUX_TEC____20251212T000000_20251212T235959_01_DJJ6LQ | jq .properties.updated,.properties.created,.properties.start_datetime,.properties.end_datetime'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")