#!/bin/sh

for FILE in `ls T*.txt`; do
	echo $FILE
	cat $FILE | sed -e 's/txname/txName/' | sed -e 's/^condition/conditionDescription/' | sed -e 's/fuzzycondition/condition/' > ${FILE}.new
done
