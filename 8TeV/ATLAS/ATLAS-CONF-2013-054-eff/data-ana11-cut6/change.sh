#!/bin/sh

cat dataInfo.txt | sed -e 's/dataid/dataId/' | sed -e 's/datatype/dataType/' > dataInfo.txt
