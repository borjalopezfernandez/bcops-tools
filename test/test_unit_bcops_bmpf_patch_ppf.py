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


def test_errors(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")
    cmd             = f'bcops_bmpf_patch_ppf -f FILE_I_DO_NOT_EXIST.EOF'
    logger.info(cmd)
    exit = os.system(cmd)
    assert( exit >> 8 == 1 )
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")


def test_patch_ppf(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('bcops')}")

    logger.info(f'copy file BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF to /data/mpf/BMPF/data/outgoing/MPL_PPF___')
    shutil.copyfile('test/data/BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF', '/data/mpf/BMPF/data/outgoing/MPL_PPF___/BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF')

    if pathlib.Path('/data/mpf/BMPF/BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF_ORIGINAL').exists():
        logger.info('remove file /data/mpf/BMPF/BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF_ORIGINAL')
        os.remove('/data/mpf/BMPF/BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF_ORIGINAL')

    if pathlib.Path('/data/mpf/BMPF/BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF_PATCHED').exists():
        logger.info('remove file /data/mpf/BMPF/BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF_PATCHED')
        os.remove('/data/mpf/BMPF/BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF_PATCHED')
    
    cmd = f'bcops_bmpf_patch_ppf -f BIO_OPER_MPL_PPF_1__20260309T000000_20260315T235959_0001.EOF'
    logger.info(cmd)
    exit = os.system(cmd)
    assert( exit >> 8 == 0 )
        
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('bcops')}")