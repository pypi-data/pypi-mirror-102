import os, glob
import pytest
import subprocess
import pytest
from NFSyndication import init as NFS_init
from NFSyndication.core import args

# test@
# Change the action associated with your option to action='store'

def test_conf():
    #We use these conditions to check the statement
    args.outputJSON = "feed-output.json"
    subscriptions = [
     'http://feedpress.me/512pixels',
     'http://www.leancrew.com/all-this/feed/',
     'http://ihnatko.com/feed/',
     'http://blog.ashleynh.me/feed']
  
    with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))
    return NFS_init()
    
def test_entrypoint():
    #Then initialize code
    return test_conf()
