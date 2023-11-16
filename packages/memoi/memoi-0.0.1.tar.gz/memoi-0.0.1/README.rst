=====
Memoi
=====

Description
===========

A generic caching mechanism for memoizing function or method calls.

Prerequisites
=============

- Python >= 3.10

Installation
============

.. code-block:: bash

  python -m pip install memoi


Example
=======

.. code-block:: python

  from datetime import datetime as dt
  from memoi import cached, TextFileRepo

  @cached(TextFileRepo('.'))
  def f(*args, **kwargs):
      return f"this is the result of the first f() call at {dt.now().isoformat()}"

  print(f())
  print(f())


This will create a a sqlite database ``memo.sqlite``, keeping track of function calls,
and a text file ``50/506f353d3ef92d51f3e57bae99367caf`` directory, containing the result of the first ``f()`` call.
Obviously the timestamp from the first function call is preserved. 

Author
======

Emanuel Schmid, schmide@ethz.ch
