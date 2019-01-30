#!/bin/bash

GREETING=$1
NAME=$2

if [[ $# -eq 0 ]]; then
 echo 'Usage: hello.sh GREETING [NAME]'
 exit 1

elif [[ $# -gt 2 ]]; then
 echo 'Usage: hello.sh GREETING [NAME]'
 exit 1

elif [[ $# -eq 1 ]]; then
 echo "$GREETING, Human!"

elif [[ $# -eq 2 ]]; then
 echo "$GREETING, $NAME!"
fi
