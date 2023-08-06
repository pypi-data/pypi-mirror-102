import os
import sys
import argparse
import logging
import time
import logging.handlers
from . import __version__, __base_path__
from . import config
from .core import args
from colorama import init, Fore, Back, Style

from functools import wraps

init(convert=True)

pathCwd = os.getcwd()
handler = logging.StreamHandler()

def exec_wrapper(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("{}Command execution took {}s{}".format(Fore.LIGHTBLACK_EX, round(end - start, 2), Style.RESET_ALL))
        return result

    return wrapper

if args.version:
      print('{}NFSyndication version: {_ver}{_rs}'.format(Fore.LIGHTBLUE_EX, _ver=__version__, _rs=Style.RESET_ALL))
      sys.exit(0)

@exec_wrapper
def run():
   if os.path.isfile(__base_path__) and os.access(__base_path__, os.R_OK):
      print('You are in directory ' + os.path.join(pathCwd))
   return config.init()

#logging.StreamHandler()
#logger = logging.getLogger()

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
logFile = 'nfsyndication-logs.log'
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

if args.verbose == 1:
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(logFile, 'w+')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)
elif args.verbose == 2:
        logger.setLevel(logging.DEBUG)
elif args.verbose == 3:
        logger.setLevel(logging.CRITICAL)

if __name__ == '__main__':
    run()