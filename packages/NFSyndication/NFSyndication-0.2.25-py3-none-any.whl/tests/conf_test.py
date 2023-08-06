import os, glob
import pytest
import subprocess
import pytest
from NFSyndication import init

# test@
import logging

logging.basicConfig(level=logging.DEBUG)
logD = logging.getLogger()

#############################################################################

def setup_module(module):
    ''' Setup for the entire module '''
    logD.info('Inside Setup')
    # Do the actual setup stuff here
    pass

def setup_function(func):
    ''' Setup for test functions '''
    if func == test_one:
        logD.info('  !!')

def test_one():
    ''' Test One '''
    logD.info('Inside Test 1')
    #assert 0 == 1
    pass

def test_two():
    ''' Test Two '''
    logD.info('Inside Test 2')
    pass

if __name__ == '__main__':
    logD.info(' About to start the tests ')
    pytest.main(args=[os.path.abspath(__file__)])
    logD.info(' Done executing the tests ')
 