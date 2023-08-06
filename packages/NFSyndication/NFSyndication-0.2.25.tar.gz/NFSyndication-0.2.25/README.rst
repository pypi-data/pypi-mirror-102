=====================
News Feed Syndication
=====================
   
.. image:: https://travis-ci.org/web-sys1/NFSyndication.svg?branch=master
   :target: https://travis-ci.org/web-sys1/NFSyndication

.. image:: https://img.shields.io/pypi/v/NFSyndication.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/NFSyndication.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/NFSyndication

.. image:: https://github.com/web-sys1/NFSyndication/workflows/CodeQL/badge.svg
   :target: https://github.com/web-sys1/NFSyndication/actions?query=workflow%3ACodeQL++
   :alt: tests

     
This is a set of scripts for aggregating RSS feeds.

.. image:: https://repl.it/badge/github/web-sys1/NFSyndication
   :target: https://repl.it/github/web-sys1/NFSyndication

Installation
------------

You can install package through the line command:

.. code:: bash

   pip install NFSyndication

*Alternatively you can install it form source code (with git prefix):* ``pip install git+https://github.com/web-sys1/NFSyndication.git``

Usage
-----
Put a list of feed URLs in ``feeds.txt`` file. One feed per line. 

Run the command:

.. code:: bash

   nfsyndication-src
   usage: nfsyndication-src [-h] [-V] [-v] [-f FILENAME [FILENAME ...]] [--outputJSON OUTPUTJSON] [--comparator-filter [COMPARATOR_FILTER]]

   News Feed Syndication - A package that read and fetch RSS feeds from the publications.

   optional arguments:
     -h, --help            show this help message and exit
     -V, --version         Print the package version and quit
     -v, --verbose         Show verbose messages
     -f FILENAME [FILENAME ...], --filename FILENAME [FILENAME ...]
                           specify which file type to use (for example: nfsyndication-src --filename=./path/to/sample.file.txt)
     --outputJSON OUTPUTJSON
                           Save feeds to output file JSON format.
     --comparator-filter [COMPARATOR_FILTER]
                           Enable the comparator. This will randomly ignore stale RSS feeds from the rendering output HTML.
   
Otherwise, you should do that through **Python** code:

.. code:: python

  from NFSyndication import init as NFS_init

  def entry_point():
    """ We use these conditions to check the statement"""
    subscriptions = [
     'http://feedpress.me/512pixels',
     'http://www.leancrew.com/all-this/feed/',
     'http://ihnatko.com/feed/',
     'http://blog.ashleynh.me/feed',
     'http://www.betalogue.com/feed/',
      ...
     ]
  
    with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))
    return NFS_init()

  """Then initialize code."""
  entry_point()
  
If you wish to do another way instead of feeds.txt, you should use pass filename to upload list of the feeds. Then run:

.. code:: bash

   nfsyndication-src --filename=path/to/feeds.txt

.. note:: Assuming nothing goes wrong, the posts will be written to ``HTML`` file.

License
-------

See LICENSE_

Bug fix
-------

After many hours of working to development, it was set up an way of path
configuration due to errors. Meanwhile, we have to set code
``os.path.dirname(os.path.realpath(__file__))`` with the globalization
of variables for source code in this package. If you encounter a problem, please report `here <https://github.com/web-sys1/NFSyndication/issues/new>`_.

This package was initially released on August 16, 2020 (under version 0.2.0). For more information about changes, see CHANGELOG_.

.. _LICENSE: https://github.com/web-sys1/NFSyndication/blob/master/LICENSE
.. _CHANGELOG: https://github.com/web-sys1/NFSyndication/blob/master/CHANGELOG.rst
