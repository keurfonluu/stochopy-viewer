stochopy-viewer
===============

|License| |Stars| |Code style: black|

**stochopy-viewer** is a Graphical User Interface (GUI) for `stochopy <https://github.com/keurfonluu/stochopy>`__. It mainly aims to show how various stochastic algorithms and their hyperparameters affect the sampling or optimization on common benchmark functions.

|GUI|

Installation
------------

The recommended way to install **stochopy-viewer** and all its dependencies is through the Python Package Index:

.. code::

   pip install git+https://github.com/keurfonluu/stochopy-viewer.git --user

Otherwise, clone and extract the package, then run from the package location:

.. code::

   pip install . --user

Usage
-----

To run **stochopy-viewer**, simply execute the command line:

.. code::

   stochopy-viewer

Otherwise, in a Python script:

.. code:: python

   from stochopy_viewer import main

   main()

.. |License| image:: https://img.shields.io/github/license/keurfonluu/stochopy-viewer
   :target: https://github.com/keurfonluu/stochopy-viewer/blob/master/LICENSE

.. |Stars| image:: https://img.shields.io/github/stars/keurfonluu/stochopy-viewer?logo=github
   :target: https://github.com/keurfonluu/stochopy-viewer

.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
   :target: https://github.com/psf/black

.. |GUI| image:: https://github.com/keurfonluu/stochopy-viewer/blob/master/.github/stochopy_viewer.png?raw=true
   :alt: stochopy_viewer
