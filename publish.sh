#!/bin/bash

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################

# Use this script to (re)publish the documentation

export PATH=/APSshare/epd/rh5-x86/bin:$PATH
export PROJECT="HDF5gateway"
export TARGET_DIR=/home/joule/SVN/subversion/small_angle

#/home/joule/SVN/subversion/small_angle/projects/hdfgateway

echo "Updating from subversion repository"
svn update

echo "rebuilding the documentation"
make clean

python extractor.py
make latexpdf
cp _build/latex/HDF5gateway.pdf ./
make html

echo "Removing the old build, if it exists"
/bin/rm -rf $TARGET_DIR/$PROJECT

echo "Copying the rebuilt web site"
cd _build
mv html $PROJECT
tar cf - $PROJECT | (cd $TARGET_DIR && tar xf -)
/bin/rm -rf $PROJECT
cd ..

echo "Done publishing $PROJECT"
