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
	not yet available online but soon


:pdf:
	not yet available online but soon


.. index:: subversion; source code

Downloads
====================================

**IgorExchange** ::

	--tba--

**subversion checkout** ::
	
	svn co https://subversion.xray.aps.anl.gov/small_angle/hdf5gateway/trunk hdf5gateway


.. include:: CHANGES


.. index:: documentation; building

Building the documentation
====================================

The documentation for *HDF5gateway* is built from .rst files and from content in
the *hdf5gateway.ipf* IgorPro procedure file by a Python script called *extractor.py*, 
located in the same directory.

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

#. copy the HTML directory to the publishing space

	--tba--

#. copy the PDF file to the publishing space

	--tba--

