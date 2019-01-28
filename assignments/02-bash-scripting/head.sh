#!/bin/bash

i=0
FILE=$1
NUM=$2
if [[ $# -eq 0 ]]; then
 echo 'Usage: head.sh FILE NUM'
 exit 1

elif [[ ! -f $FILE ]]; then
 echo "$FILE is not a file"
 exit 1

elif [[ -f $FILE ]]; then
 if [[ $NUM -eq 0 ]]; then
 #echo "missing number default 3"
  NUM=3
 fi
 if [[ $NUM =~ ^-?[0-9]+$ ]]; then
  NUM=$NUM
 fi
 while read line; do
   if [ $i -lt $NUM ]; then
    let i++
	echo "$line"
   fi
  done < $FILE
 exit 0
fi
