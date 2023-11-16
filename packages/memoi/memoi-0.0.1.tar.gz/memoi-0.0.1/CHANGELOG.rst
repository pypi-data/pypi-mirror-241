=========
Changelog
=========

Release 0.0.1
=============

Description
-----------

Minimum Viable Product of a result caching function decorator.

Added
-----

- decorator ``cached``: providing a caching mechanism for return values, so the function is not executed the next time when it is called with the same arguments.
- class ``TextFileRepo``: for caching return values of functions returning strings as text files in a configurable directory.
