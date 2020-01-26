#!/usr/bin/env python

'''
extract rest documentation from IgorPro procedure file

Lines to be extracted will be marked similar to this example::
    
    //@+
    // PRJ_TestFile(parentDir, sourceFile)
    // -------------------------------------------------------------------------------------------------------------
    //
    //  Reads HDF5 file sourceFile into a subfolder of IgorPro folder parentDir.
    //  Then writes the structure from that subfolder to a new HDF5 file: "test_"+sourceFile
    //  Assumes that sourceFile is only a file name, with no path components, in the present working directory.
    //  Returns the name (string) of the new HDF5 file written.
    //
    //@-

All extracted lines must begin with "//\t" (which will be stripped by this routine) 
and otherwise obey all rest formatting rules, including consistent indentation
and section underlining symbols.
'''


import os
import sphinx
import sys


START_SPHINX = '//@+'
END_SPHINX = '//@-'
DOCUMENTATION_TRIGGERS = (START_SPHINX, END_SPHINX)
DOC_PREFIX = '//\t'
PREFIX_LEN = len(DOC_PREFIX)


def extractor(procedurefile, rstfile):
    if not os.path.exists(procedurefile):
        return False
    showlines = False
    t = []
    t.append('.. DO NOT EDIT!  This file is automatically built by extractor.py.')
    for line in open(procedurefile).readlines():
        if len(line) > 3 and line[0:4] in DOCUMENTATION_TRIGGERS:
            showlines = line[3] == '+'
            if showlines:
                t.append('')
        else:
            if showlines and line.startswith(DOC_PREFIX):
                s = line.rstrip()
                s = s[PREFIX_LEN:]
                t.append(s)
    open(rstfile, 'w').write('\n'.join(t))
    return True


def force_rebuild_all(parent = '_build'):
    '''
    Delete the pickle file.
    
    :param str parent: path to *build* subdirectory (either ``build`` or ``_build``)
    '''
    pickle_file = parent+'/doctrees/environment.pickle'
    if os.path.exists(pickle_file):
        os.remove(pickle_file)


if __name__ == "__main__":
    extractor('HDF5gateway.ipf', 'README.rst')
    force_rebuild_all()
    args = [sys.argv[0]] + "-b html -d _build/doctrees . _build/html".split()
    sphinx.main(args)
