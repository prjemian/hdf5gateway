.. $Id$

============================================================
Administrative Matters
============================================================

Author
====================================

:Author:
	Pete R. Jemian
	jemian@anl.gov

.. index:: documentation; pdf, documentation; html

Documentation
====================================

:html:
	http://hdf5gateway.readthedocs.org


:pdf:
	http://hdf5gateway.readthedocs.org/en/latest/_downloads/HDF5gateway.pdf


.. index:: subversion; source code

Downloads
====================================

.. index:: IgorExchange

**IgorExchange** ::

	http://www.igorexchange.com/project/HDF5gateway

Just the most recent IgorPro procedure file (text) from the development trunk:
	http://subversion.xray.aps.anl.gov/small_angle/hdf5gateway/trunk/HDF5gateway.ipf


**subversion checkout** ::
	
	svn co https://subversion.xray.aps.anl.gov/small_angle/hdf5gateway/trunk hdf5gateway


.. include:: CHANGES

.. include:: KNOWN_PROBLEMS


.. index:: documentation; building

Building the documentation
====================================

The documentation for *HDF5gateway* is built from .rst files and from content in
the *hdf5gateway.ipf* IgorPro procedure file by a Python script called *extractor.py*, 
located in the same directory.

The current documentation was built: |today|.

Required:

* Python
* Sphinx
* LaTeX

.. rubric:: How to build the documentation

#. change to the directory with the file *extractor.py*
#. extract the docs from the .ipf file and build the HTML docs::

	python extractor.py

#. build the LaTeX and then PDF files::

	make latexpdf

#. copy the PDF file to the source directory and rebuild the HTML::

	cp _build/latex/HDF5gateway.pdf ./
	python extractor.py

#. copy the rebuilt HTML directory to the publishing space

	--tba--

License
====================================

Copyright (c) 2012 University of Chicago. All rights reserved.
See the :download:`LICENSE` file for details.
