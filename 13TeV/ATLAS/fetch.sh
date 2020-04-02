#!/bin/sh

E="ATLAS"

# cp -r ~/git/smodels-database/13TeV/$E/* .
for dir in `ls -d ~/git/smodels-database/13TeV/$E/*`; do
	test -e $dir/globalInfo.txt && {
	localdir=`echo $dir | sed -e 's;/home/walten/git/smodels-database/13TeV/ATLAS/;;'`;
	echo $localdir;
	rsync -a --delete $dir/* $localdir
#	rm -r $localdir
	};
done
