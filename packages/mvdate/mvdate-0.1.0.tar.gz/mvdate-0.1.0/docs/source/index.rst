Welcome to mvdate documentation
===============================

``mvdate`` is a small utility written in `Python <https://python.org>`_ for moving files based on the last modified
date. Input is a directory path (default ``./``), a file extension without the period (default ``jpg``) and a
destination directory (default ``./``). A new directory structure is then created based on the ``YYYY/mm/dd``
(year/month/day) of files with the given extension and each file is moved into the directory reflecting its creation
date. Optionally it is possible to control the level of nesting, for example moving only to ``YYYY`` (year) directory,
or grouping files right down to the ``mm`` (minute) files were created.

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   motivation
   installation
   usage
   contributing

.. toctree::
   :maxdepth: 2
   :caption: API

   api
