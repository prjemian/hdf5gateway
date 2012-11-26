#!/bin/bash

########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################

# Use this script to (re)publish the documentation

# TODO: this needs to be fixed!!!

/bin/does.not.exist.so.will.stop.here.with.an.error

export PROJECT="HDF5gateway"
export SOURCE_DIR="build"
export TARGET_DIR="/home/joule/SVN/subversion/smang/ "
export MAKE_TARGET="all"
export MAKE_DIR="doc"

echo "Updating from subversion repository"
svn update

cd $MAKE_DIR

echo "rebuilding the documentation"
make clean
make $MAKE_TARGET

cd $SOURCE_DIR
echo "Removing the old build, if it exists"
/bin/rm -rf $PROJECT

echo "Copying the rebuilt web site"
mv html $PROJECT
tar cf /tmp/ball.tar $PROJECT
cd $TARGET_DIR
tar xf /tmp/ball.tar
echo "Done publishing $PROJECT"


#basic scheme::
#
#	python extractor.py
#	make latexpdf
#	cp _build/latex/HDF5gateway.pdf ./
#	make html
#	# copy the _build/html directory to the publishing point
