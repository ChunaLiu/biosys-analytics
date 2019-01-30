#!/bin/bash

PWD="../../data/gapminder"
cd $PWD
files=./*
INITIAL=$1
check=0
i=1
shopt -s nocasematch #case insensitive

for file in $(ls $files | sort)
do 
 filename="${file##*/}"
# basename="$(echo "$filename" | cut -f1 -d '.')"
 basename="${filename%%.*}"

 if [[ $# -eq 0 ]]; then
  echo  "$i $basename"
  let i++
  check=1
 elif [[ ${#INITIAL} -eq 1 ]]; then
  if [[ "$basename" =~ ^${INITIAL} ]]; then
   echo "$i $basename"
   let i++
   check=1
  fi
 elif [[ $INITIAL =~ ^\[ ]]; then
   if [[ "$basename" =~ ^${INITIAL} ]]; then
    echo "$i $basename"
	let i++
    check=1
   fi
 fi
done

if [[ $check -eq 0 ]]; then
 echo "There are no countries starting with \"$INITIAL\""
fi
