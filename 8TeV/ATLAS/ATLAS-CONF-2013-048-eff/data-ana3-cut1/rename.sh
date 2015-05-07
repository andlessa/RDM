#!/bin/sh

FILE=T1bbqq.txt

for FILE in `ls T*.txt`; do
	cat $FILE | sed -e 's/txname/txName/' | sed -e 's/^condition/conditionDescription/' | sed -e 's/fuzzycondition/condition/' | tee ${FILE}.new
	cp ${FILE}.new ${FILE}
done
