gdalinfo
========

A cffi-based wrapper for just the GDALInfo() function from GDAL.

Returns GIS metadata from a filename as JSON.

On pypy, ``import sqlite3`` may conflict with ``import gdalinfo``, 
they both use a version of the sqlite library. Use ``pypy -m _sqlite3_build``
to build the extension against system sqlite3, and replace the one that
came with the pypy distribution.