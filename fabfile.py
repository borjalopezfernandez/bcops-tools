import glob
import os

from fabric import task, executor
from loguru import logger


@task
def build(context):
    '''
    Build bcops binary wheel distribution
    '''
    cmd = 'python setup.py bdist_wheel'
    logger.info(cmd)
    context.run(cmd)


@task
def install(context):
    '''
    Install bcops latest built package with pip
    '''
    list_of_files   = glob.glob('dist/bcops*')
    latest_package  = max(list_of_files, key=os.path.getctime)
    cmd             = f"pip install {latest_package}"
    logger.info(cmd)
    context.run(cmd)


@task
def uninstall(context):
    '''
    Uninstall bcops package with pip
    '''
    cmd = 'pip uninstall -y bcops'
    logger.info(cmd)
    context.run(cmd)


@task
def update(context):
    '''
    Update bcops python package:
    > build 
    > uninstall
    > install
    '''
    build(context)
    uninstall(context)
    install(context)


@task
def test(context):
    '''
    Execution of unit tests:
    '''
    test_unit_bcops_maap_query_product(context)
    test_unit_bcops_maap_query_datatake(context)
    
    
@task
def test_unit_bcops_maap_query_datatake(context):
    '''
    Execution of unit test test_unit_bcops_maap_query_datatake.py 
    '''
    cmd = 'pytest -rpf -s test/test_unit_bcops_maap_query_datatake.py'
    logger.info(cmd)
    context.run(cmd)


@task
def test_unit_bcops_maap_query_product(context):
    '''
    Execution of unit test main_test_unit_bcops_product.py 
    '''
    cmd = 'pytest -rpf -s test/test_unit_bcops_maap_query_product.py'
    logger.info(cmd)
    context.run(cmd)
